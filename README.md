# 오산 출장마사지 사이트

경기도 오산시 전지역 방문 관리 서비스(출장마사지·홈타이) 안내 정적 사이트입니다.
오산은 행정구(區)가 없는 단일 도시이므로 **오산시 메인 → 대표동 → 역세권 → 생활권** 구조로 설계했습니다.

**상호**: 바로 GO
**예약전화**: 0508-202-4719
**문의(텔레그램)**: https://t.me/googleseolab

## 구조

- **정적 HTML 사이트** — 어느 호스팅(Cloudflare Pages, GitHub Pages, 웹서버)에서든 그대로 서빙 가능
- **build.py** + **content/** — 페이지를 Python으로 정의하고 정적 HTML 생성
- **생성물** — 각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`

```
build.py                       # 빌드 스크립트
content/
  site.py                      # 상호·전화·도메인·메뉴(NAV)
  main.py                      # 메인 페이지 (사이트 루트 /)
  areas.py                     # 지역별 페이지 (10개 동·생활권)
  stations.py                  # 역세권 페이지 (6개)
  areas_and_stations.py        # 생활권 페이지 (10개)
  info.py                      # 정보 페이지 (예약·확인사항·가이드·약관·고객센터)
assets/
  style.css                    # 프리미엄 다크 팔레트 + 오렌지 + 컴포넌트 오버레이 + Pretendard
  nav.js                       # 모바일 네비게이션
index.html                     # 생성된 메인 페이지 (루트)
area/ station/ ...             # 생성된 하위 페이지
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## URL 구조

- 메인: `/`
- 지역: `/jungang-dong/`, `/daewon-area/` …
- 역세권: `/station/osan-station/` …
- 생활권: `/area/segyeo-newtown/` …
- URL·메뉴명에는 `출장마사지`, `홈타이`, `massage` 등 키워드를 넣지 않는다.

## SEO 운영 원칙

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리
- 오산은 구 단위가 없으므로 구별 페이지를 만들지 않는다.
- 핵심 역세권은 오산역·오산대역·세마역, 병점/서동탄/진위역은 인접 생활권으로만 처리
- 메뉴명·URL에 키워드 대량 나열 없음 — Title/H1/첫 문단에서만 자연스럽게 사용
- 모든 페이지 본문은 고유 작성 (지역명만 바꾼 복붙 없음)
- 내부 링크 롱테일 키워드 강화 + 권위 있는 외부 사이트(오산시청·코레일 등) 링크
- E-E-A-T / 도움되는 콘텐츠 / Who·How·Why 원칙 반영, YMYL 신뢰 신호 강화
- 방문형 서비스(오프라인 주소 없음)이므로 LocalBusiness 대신 Organization/HealthAndBeautyBusiness 스키마 사용

## 색인(인덱싱) 자동화

빌드 시 자동 생성:
- `sitemap.xml` — `lastmod`·`changefreq`·`priority` 포함 (색인 허용 페이지만)
- `rss.xml` — RSS 2.0 피드 (신규/갱신 발견 가속)
- `robots.txt` — 구글·빙·네이버(Yeti)·다음 허용 + 사이트맵/RSS 안내
- 메인페이지 `<meta name="naver-site-verification">` 등록 완료

### IndexNow (빙·네이버 즉시 통보) — 키 파일 셋업 완료
- 키 파일: `5b49b75895edd307d475da6a04ce901c.txt` (사이트 루트에 배포되어 공개 접근 가능)
- **첫 일괄 통보** (로컬에서 1회):
  ```bash
  python3 build.py            # 최신 sitemap.xml 생성
  python tools/indexnow.py    # sitemap 의 모든 URL 을 빙·네이버에 즉시 통보
  ```
- **글 올릴 때마다** — 특정 URL만 통보:
  ```bash
  python tools/indexnow.py https://osan-massage1.pages.dev/새글경로/
  ```

### 구글 Indexing API (구글은 IndexNow 미참여)
1. Google Cloud → Indexing API 사용 설정 → 서비스 계정 JSON 키를 `tools/service-account.json` 로 저장 (`.gitignore` 처리됨, 커밋 안 됨)
2. Search Console 에서 서비스 계정 이메일을 사이트 **소유자**로 추가
3. `pip install google-auth requests`
4. 실행: `python tools/google_indexing.py` (또는 특정 URL 인자)

### 사이트맵 ping (참고)
구글·빙 모두 sitemap ping 엔드포인트를 폐지했습니다(2023). `tools/ping_sitemap.py` 는 IndexNow 를 호출하고 폐지된 ping 을 best-effort 로 시도합니다. **최초 1회는 Search Console·네이버 서치어드바이저에 `sitemap.xml` 을 직접 제출**하세요.

> 가장 빠른 순서: ① IndexNow(빙·네이버) → ② 구글 Indexing API → ③ Search Console/서치어드바이저 사이트맵 제출

## 디자인

- **프리미엄 다크 팔레트**: 딥 옵시디언 네이비 + 오렌지 #FF6B35 + 샴페인 골드
- **컴포넌트 오버레이**: 글래스모피즘, 시인(sheen) 그라데이션, 글로우 — `:root` 토큰 위에 레이어로 적용
- **Pretendard 폰트**: 한국식 산세리프 (최상의 가독성)
- **푸터**: 웹사이트 제작문의 · 제휴문의 오렌지 버튼 + 텔레그램 링크
- **반응형·접근성·성능**: 시맨틱 HTML, WAI-ARIA, 정적 HTML(CDN 친화)

## 배포 전 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행
3. Google Search Console에 `sitemap.xml` 제출
