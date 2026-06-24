#!/usr/bin/env python3
"""구글 Indexing API 색인 통보 (구글은 IndexNow 미참여).

구글에 URL 갱신/삭제를 즉시 알립니다. IndexNow(빙·네이버)와 별개로 동작합니다.

사전 준비 (1회):
  1) Google Cloud 프로젝트 생성 → "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드 → tools/service-account.json 로 저장
     (이 파일은 비밀이므로 .gitignore 에 등록되어 커밋되지 않습니다)
  3) Google Search Console 에서 해당 서비스 계정 이메일을
     사이트 "소유자(Owner)"로 추가
  4) 의존성 설치: pip install google-auth requests

사용법:
  # sitemap.xml 의 모든 URL 갱신 통보
  python tools/google_indexing.py

  # 특정 URL 만 통보
  python tools/google_indexing.py https://osan-massage1.pages.dev/jungang-dong/

  # 삭제 통보
  python tools/google_indexing.py --delete https://osan-massage1.pages.dev/old/

참고: 구글 Indexing API 는 공식적으로 JobPosting/BroadcastEvent 용도로 안내되지만,
실무에서 일반 페이지 색인 가속에 널리 사용됩니다. 효과는 보장되지 않으며,
정식 경로는 Search Console 사이트맵 제출입니다.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SA_PATH = os.path.join(ROOT, "tools", "service-account.json")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def urls_from_sitemap() -> list:
    sm = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(sm):
        raise SystemExit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    with open(sm, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def main() -> None:
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        raise SystemExit("의존성이 필요합니다: pip install google-auth requests")

    if not os.path.exists(SA_PATH):
        raise SystemExit(f"서비스 계정 키가 없습니다: {SA_PATH}")

    args = sys.argv[1:]
    notify_type = "URL_UPDATED"
    if args and args[0] == "--delete":
        notify_type = "URL_DELETED"
        args = args[1:]
    urls = args or urls_from_sitemap()
    if not urls:
        raise SystemExit("통보할 URL 이 없습니다.")

    creds = service_account.Credentials.from_service_account_file(SA_PATH, scopes=SCOPES)
    session = AuthorizedSession(creds)

    print(f"구글 Indexing API ({notify_type}): {len(urls)}개 URL")
    ok = 0
    for url in urls:
        resp = session.post(ENDPOINT, json={"url": url, "type": notify_type}, timeout=30)
        status = "OK" if resp.status_code == 200 else f"ERR {resp.status_code}"
        if resp.status_code == 200:
            ok += 1
        print(f"  [{status}] {url}")
        if resp.status_code != 200:
            print("     " + resp.text[:200])
    print(f"완료: {ok}/{len(urls)} 성공")


if __name__ == "__main__":
    main()
