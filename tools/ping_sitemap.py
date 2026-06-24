#!/usr/bin/env python3
"""사이트맵 핑 (참고용).

주의: 구글은 2023년 6월, 빙은 그 이전에 sitemap "ping" 엔드포인트를 폐지했습니다.
따라서 ping 은 더 이상 권장 경로가 아니며, 이 스크립트는 호환성을 위해 남겨둡니다.

가장 빠른 색인 경로(권장 순서):
  1) IndexNow   → python tools/indexnow.py        (빙·네이버 즉시 통보)
  2) 구글 Indexing API → python tools/google_indexing.py
  3) Google Search Console / 네이버 서치어드바이저에 sitemap.xml 직접 제출 (최초 1회)

이 스크립트는 1)을 호출한 뒤, 폐지된 ping 도 best-effort 로 시도합니다.
"""
import os
import sys
import urllib.parse
import urllib.request

BASE = "https://osan-massage1.pages.dev"
SITEMAP = f"{BASE}/sitemap.xml"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 폐지되었으나 호환성 위해 남겨둔 ping 엔드포인트 (실패할 수 있음)
LEGACY_PING = [
    "https://www.google.com/ping?sitemap=",
    "https://www.bing.com/ping?sitemap=",
]


def main() -> None:
    # 권장 경로 먼저: IndexNow
    print("→ IndexNow 통보 실행 (권장 경로)")
    os.system(f'"{sys.executable}" "{os.path.join(ROOT, "tools", "indexnow.py")}"')

    print("\n→ (참고) 폐지된 sitemap ping best-effort 시도")
    enc = urllib.parse.quote(SITEMAP, safe="")
    for base in LEGACY_PING:
        url = base + enc
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:
                print(f"  [{resp.status}] {url}")
        except Exception as e:  # noqa: BLE001
            print(f"  [폐지/실패] {base} — {e}")
    print("\nℹ️  최초 1회는 Search Console·네이버 서치어드바이저에 sitemap.xml 을 직접 제출하세요.")


if __name__ == "__main__":
    main()
