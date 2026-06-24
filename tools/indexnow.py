#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 (빙·네이버·Yandex 등 IndexNow 참여 엔진).

글을 올리거나 페이지를 갱신할 때마다 실행하면 검색엔진에 즉시 색인 요청을 보냅니다.
표준 라이브러리만 사용하므로 별도 설치가 필요 없습니다.

사용법:
  # 1) 첫 일괄 통보 — sitemap.xml 의 모든 URL 을 통보
  python tools/indexnow.py

  # 2) 글 올릴 때마다 — 특정 URL 만 통보
  python tools/indexnow.py https://osan-massage1.pages.dev/jungang-dong/ https://osan-massage1.pages.dev/

설명:
  - api.indexnow.org 에 한 번 보내면 참여 엔진(빙 등)에 공유되지만,
    네이버·빙에 확실히 전달되도록 각 엔드포인트에도 직접 통보합니다.
  - 키 파일(<key>.txt)은 사이트 루트에 배포되어 있어야 합니다.
"""
import glob
import json
import os
import re
import sys
import urllib.request
import urllib.error

HOST = "osan-massage1.pages.dev"
SCHEME = "https"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# IndexNow 엔드포인트 (한 곳에 보내면 공유되지만, 도달 보장을 위해 다중 통보)
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",  # 네이버
    "https://yandex.com/indexnow",
]


def find_key() -> str:
    """사이트 루트의 <32hex>.txt 키 파일에서 IndexNow 키를 읽는다."""
    for path in glob.glob(os.path.join(ROOT, "*.txt")):
        name = os.path.splitext(os.path.basename(path))[0]
        if re.fullmatch(r"[0-9a-fA-F]{8,128}", name):
            with open(path, encoding="utf-8") as f:
                content = f.read().strip()
            if content == name:
                return name
    raise SystemExit("IndexNow 키 파일(<key>.txt)을 사이트 루트에서 찾을 수 없습니다.")


def urls_from_sitemap() -> list:
    sm = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(sm):
        raise SystemExit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    with open(sm, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def notify(endpoint: str, payload: dict) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint, data=data, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  [{resp.status}] {endpoint}")
    except urllib.error.HTTPError as e:
        # 200/202 외 코드도 엔진별로 정상 처리될 수 있음 (예: 빙 200, 일부 202)
        print(f"  [{e.code}] {endpoint} — {e.reason}")
    except Exception as e:  # noqa: BLE001
        print(f"  [ERR] {endpoint} — {e}")


def main() -> None:
    key = find_key()
    key_location = f"{SCHEME}://{HOST}/{key}.txt"
    urls = sys.argv[1:] or urls_from_sitemap()
    if not urls:
        raise SystemExit("통보할 URL 이 없습니다.")

    print(f"IndexNow 통보: {len(urls)}개 URL / host={HOST}")
    payload = {
        "host": HOST,
        "key": key,
        "keyLocation": key_location,
        "urlList": urls,
    }
    for ep in ENDPOINTS:
        notify(ep, payload)
    print("완료. (빙·네이버는 키 파일 검증 후 색인 큐에 반영합니다)")


if __name__ == "__main__":
    main()
