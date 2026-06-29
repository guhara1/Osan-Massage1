import json
from .site import BRAND, BASE_URL, PHONE

_BASE = BASE_URL.rstrip("/")

# 메타 설명 (80자 이내)
DESC = "오산 출장마사지·홈타이 예약 전 오산역, 오산대역, 세마역, 세교, 대원 생활권을 확인하세요."

# 자주 묻는 질문 (FAQ 스키마)
_FAQ = [
    ("오산역 근처도 예약 가능한가요?",
     "오산역은 중앙동, 원동, 오산터미널 인접 생활권과 함께 확인할 수 있습니다. 정확한 방문 주소와 희망 시간을 먼저 확인하는 방식이 좋습니다."),

    ("오산대역과 세교는 따로 페이지를 만들어야 하나요?",
     "가능합니다. 오산대역 페이지는 역세권과 이동 기준 중심으로, 세교신도시 생활권 페이지는 수청동·신장동 인접 생활권 중심으로 작성하는 것이 좋습니다."),

    ("대원1동과 대원2동을 각각 만들어야 하나요?",
     "실제 행정동은 분리되어 있으므로 만들 수 있습니다. 다만 1차에서는 대원 생활권으로 먼저 묶고, 유입이 생기면 대원1동·대원2동을 세부 페이지로 확장하는 것이 좋습니다."),

    ("신장1동과 신장2동은 어떻게 처리하나요?",
     "1차에서는 신장 생활권으로 통합하고, 2차에서 신장1동과 신장2동을 나누는 방식이 좋습니다. 신장1동은 오산대역·수청동, 신장2동은 세교지구와 연결합니다."),

    ("병점역이나 서동탄역도 오산 페이지로 만들어도 되나요?",
     "병점역과 서동탄역은 화성시 성격이 강하므로 오산에서는 인접 생활권으로만 설명하는 것이 좋습니다."),
]

# FAQ 스키마 생성
_faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "@id": f"#faq-{i+1}",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for i, (q, a) in enumerate(_FAQ)
    ],
}
_faq_schema_str = json.dumps(_faq_schema, ensure_ascii=False, indent=2)

# Organization 스키마 (방문형 서비스 — 오프라인 주소 없음, LocalBusiness 미사용)
_org_schema = {
    "@context": "https://schema.org",
    "@type": "HealthAndBeautyBusiness",
    "name": BRAND,
    "telephone": PHONE,
    "url": _BASE + "/",
    "image": _BASE + "/assets/og-image.png",
    "description": "오산시 출장마사지·홈타이 안내 사이트",
    "areaServed": {"@type": "AdministrativeArea", "name": "경기도 오산시"},
    "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "opens": "00:00",
        "closes": "23:59",
    },
}
_org_schema_str = json.dumps(_org_schema, ensure_ascii=False, indent=2)

# BreadcrumbList 스키마 (메인 페이지는 홈만)
_breadcrumb_schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "홈", "item": _BASE + "/"}
    ],
}
_breadcrumb_schema_str = json.dumps(_breadcrumb_schema, ensure_ascii=False, indent=2)

_EXTRA_HEAD = f"""<meta name="naver-site-verification" content="d9586ee6fc3667eab9779ad653afb88a20e23e03" />
<script type="application/ld+json">
{_org_schema_str}
</script>
<script type="application/ld+json">
{_breadcrumb_schema_str}
</script>
<script type="application/ld+json">
{_faq_schema_str}
</script>"""

_HERO = """<div class="hero">
  <div class="hero-inner">
    <div class="hero-content">
      <div class="hero-badge">오산시 전지역 방문 관리</div>
      <h1 class="hero-title">오산 출장마사지<br><span class="hero-accent">오산 홈타이</span><br>지역별 예약 안내</h1>
      <p class="hero-lead">오산역, 오산대역, 세마역, 세교, 중앙동, 대원, 신장, 초평 생활권별 방문 가능 지역과 예약 전 확인사항을 안내합니다.</p>
      <div class="hero-cta">
        <a href="#areas" class="btn btn-primary">지역별 안내 보기</a>
        <a href="#stations" class="btn btn-secondary">가까운 역 찾기</a>
        <a href="/reservation/" class="btn btn-secondary">예약 안내 보기</a>
        <a href="/check/" class="btn btn-secondary">이용 전 확인사항</a>
      </div>
    </div>
    <div class="hero-media">
      <img src="/assets/hero-spa.webp" alt="오산 출장마사지·홈타이 프리미엄 관리 공간 — 아늑한 조명의 2인 관리실" width="1680" height="940" loading="eager" decoding="async" fetchpriority="high">
    </div>
  </div>
  <div class="hero-stats">
    <div class="stat">
      <div class="stat-number">10</div>
      <div class="stat-label">지역 페이지</div>
    </div>
    <div class="stat">
      <div class="stat-number">6</div>
      <div class="stat-label">역세권 안내</div>
    </div>
    <div class="stat">
      <div class="stat-number">10</div>
      <div class="stat-label">생활권 안내</div>
    </div>
    <div class="stat">
      <div class="stat-number">24H</div>
      <div class="stat-label">상담 가능</div>
    </div>
  </div>
</div>"""

PAGE = {
    "path": "",
    "title": "오산 출장마사지｜오산역·오산대역·세마역 홈타이 지역 안내",
    "desc": DESC,
    "h1": "오산 출장마사지 · 오산 홈타이 지역별 예약 안내",
    "hero": _HERO,
    "breadcrumb": [],
    "extra_head": _EXTRA_HEAD,
    "body": """
<section id="criteria">
  <h2>오산에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
  <p>오산시는 경기도 남부에 위치한 도시로, 다른 도시와 달리 행정구(區)가 따로 없는 단일 행정 체계의 도시입니다. 그래서 오산에서 출장마사지나 홈타이 방문 관리를 찾을 때는 구 단위가 아니라 <strong>오산역 중심권, 세교신도시, 세마역 생활권, 대원·원동 생활권, 초평·남촌 생활권</strong>이라는 실제 생활권 단위로 자신의 위치를 파악하는 것이 가장 정확합니다.</p>
  <p>오산역 주변은 <a href="/jungang-dong/">중앙동</a>과 원동, 오산시청, 오산터미널 생활권과 연결됩니다. 오산 원도심의 상권과 행정 중심이 모여 있어 방문 수요가 가장 많이 형성되는 권역입니다. <a href="/station/osandae-station/">오산대역</a> 주변은 수청동과 세교 생활권 검색 의도가 강하며, 신축 오피스텔과 아파트 단지가 밀집해 있습니다.</p>
  <p><a href="/station/sema-station/">세마역</a> 주변은 세마동, 양산동, 지곶동, 북오산 생활권으로 잡습니다. <a href="/chopyeong-dong/">초평동</a>과 갈곶·고현 방향은 도심에서 다소 떨어져 있어 차량 이동 기준과 추가 이동비 확인이 특히 중요합니다. 예약 전에 자신의 주소가 어느 생활권에 속하고, 가장 가까운 역이 어디인지, 기본 이동권 범위에 포함되는지를 먼저 확인하면 예약 과정이 훨씬 원활해집니다.</p>
</section>

<section id="areas">
  <h2>오산 대표 지역별 방문 가능 지역 안내</h2>
  <div class="card-grid">
    <a href="/jungang-dong/" class="card">
      <h3>중앙동</h3>
      <p>오산역, 오산시청, 오산 원도심 인접 생활권</p>
    </a>
    <a href="/daewon-area/" class="card">
      <h3>대원 생활권</h3>
      <p>원동, 갈곶동, 고현동, 오산역 남부 인접권</p>
    </a>
    <a href="/namchon-dong/" class="card">
      <h3>남촌동</h3>
      <p>궐동, 청학동, 오산대역 인접 생활권</p>
    </a>
    <a href="/sinjang-area/" class="card">
      <h3>신장 생활권</h3>
      <p>수청동, 은계동, 내삼미동, 세교 생활권</p>
    </a>
    <a href="/sema-dong/" class="card">
      <h3>세마동</h3>
      <p>세마역, 양산동, 지곶동, 세교 북부 생활권</p>
    </a>
    <a href="/chopyeong-dong/" class="card">
      <h3>초평동</h3>
      <p>가장동, 서동, 누읍동, 갈곶·고현 인접 생활권</p>
    </a>
    <a href="/daewon-1-dong/" class="card">
      <h3>대원1동</h3>
      <p>오산역·원동 중심 생활권과 연결</p>
    </a>
    <a href="/daewon-2-dong/" class="card">
      <h3>대원2동</h3>
      <p>고현동·갈곶동·세교 남부 인접 생활권과 연결</p>
    </a>
    <a href="/sinjang-1-dong/" class="card">
      <h3>신장1동</h3>
      <p>수청동·은계동·오산대역 인접 생활권과 연결</p>
    </a>
    <a href="/sinjang-2-dong/" class="card">
      <h3>신장2동</h3>
      <p>세교지구·내삼미동·수청동 인접 생활권과 연결</p>
    </a>
  </div>
</section>

<section id="stations">
  <h2>오산 주요 지하철역별 홈타이 안내</h2>
  <p>오산시의 핵심 역세권은 오산역, 오산대역, 세마역입니다. 병점역·서동탄역·진위역은 인접 도시 성격이 강하므로 인접 생활권 기준으로만 안내합니다.</p>
  <div class="card-grid">
    <a href="/station/osan-station/" class="card">
      <h3>오산역</h3>
      <p>중앙동, 원동, 오산터미널 인접 생활권입니다. 방문 주소와 건물 출입 가능 여부를 먼저 확인하세요.</p>
    </a>
    <a href="/station/osandae-station/" class="card">
      <h3>오산대역</h3>
      <p>수청동, 세교, 남촌동 인접 생활권입니다. 자택·숙소·오피스텔 이용 가능 여부를 먼저 확인하세요.</p>
    </a>
    <a href="/station/sema-station/" class="card">
      <h3>세마역</h3>
      <p>세마동, 양산동, 지곶동 인접 생활권입니다. 차량 이동 기준과 추가 이동비 여부를 확인하세요.</p>
    </a>
    <a href="/station/byeongjeom-nearby-area/" class="card">
      <h3>병점역 인접</h3>
      <p>오산 북부 이동 기준 안내 (화성시 인접권)</p>
    </a>
    <a href="/station/seodongtan-nearby-area/" class="card">
      <h3>서동탄역 인접</h3>
      <p>세마·북오산 이동 기준 안내 (화성·오산 경계)</p>
    </a>
    <a href="/station/jinwi-nearby-area/" class="card">
      <h3>진위역 인접</h3>
      <p>초평·갈곶 이동 기준 안내 (평택시 인접권)</p>
    </a>
  </div>
</section>

<section id="lifestyle">
  <h2>오산 생활권별 예약 기준</h2>
  <p>생활권 페이지는 지역 페이지와 역 페이지 사이를 연결하는 중간 허브 역할을 합니다. 지역과 역을 함께 묶어 보면 더 정확한 방문 주소와 이동 시간을 확인할 수 있습니다.</p>
  <div class="card-grid">
    <a href="/area/osan-station-jungang/" class="card">오산역·중앙동</a>
    <a href="/area/osandae-sucheong/" class="card">오산대역·수청동</a>
    <a href="/area/sema-dong/" class="card">세마역·세마동</a>
    <a href="/area/segyeo-newtown/" class="card">세교신도시</a>
    <a href="/area/daewon-won-dong/" class="card">대원·원동</a>
    <a href="/area/namchon-gwol-dong/" class="card">남촌·궐동</a>
    <a href="/area/sinjang-sucheong/" class="card">신장·수청</a>
    <a href="/area/chopyeong-gajang/" class="card">초평·가장동</a>
    <a href="/area/galgot-gohyeon/" class="card">갈곶·고현</a>
    <a href="/area/osan-ic-logistics/" class="card">오산 IC·물류 인접</a>
  </div>
</section>

<section id="check">
  <h2>오산 홈타이 예약 전 확인사항</h2>
  <p>예약을 진행하기 전에 다음 항목들을 먼저 확인하면 예약 과정이 훨씬 수월합니다. 자세한 내용은 <a href="/check/">이용 전 확인사항</a> 페이지에서 확인하세요.</p>
  <ul>
    <li><strong>방문 가능 주소 확인</strong> — 자택, 숙소, 오피스텔 등 정확한 방문 주소와 건물 유형 확인</li>
    <li><strong>예약 가능 시간 확인</strong> — 희망 예약 시간이 가능한지 미리 확인</li>
    <li><strong>추가 이동비 여부 확인</strong> — 기본 이동권 외 추가 이동비 발생 여부</li>
    <li><strong>건물 출입 방식 확인</strong> — 공동현관, 자동문, 경비 확인 등</li>
    <li><strong>자택·숙소·오피스텔 이용 기준 확인</strong> — 서비스 제공 장소 기준</li>
    <li><strong>결제 방식 확인</strong> — 현금, 계좌이체, 카드 등 가능한 결제 수단</li>
    <li><strong>예약 변경·취소 기준 확인</strong> — 변경·취소 수수료 및 절차</li>
    <li><strong>개인정보 처리 기준 확인</strong> — 개인정보 수집·이용·보관 방식</li>
    <li><strong>불법·선정적 서비스 불가 안내</strong> — 건전한 관리 서비스만 제공</li>
  </ul>
</section>

<section id="faq">
  <h2>오산 출장마사지 자주 묻는 질문</h2>
  <dl class="faq-list">
    <dt id="faq-1">오산역 근처도 예약 가능한가요?</dt>
    <dd>오산역은 중앙동, 원동, 오산터미널 인접 생활권과 함께 확인할 수 있습니다. 정확한 방문 주소와 희망 시간을 먼저 확인하는 방식이 좋습니다.</dd>

    <dt id="faq-2">오산대역과 세교는 따로 페이지를 만들어야 하나요?</dt>
    <dd>가능합니다. 오산대역 페이지는 역세권과 이동 기준 중심으로, 세교신도시 생활권 페이지는 수청동·신장동 인접 생활권 중심으로 작성하는 것이 좋습니다.</dd>

    <dt id="faq-3">대원1동과 대원2동을 각각 만들어야 하나요?</dt>
    <dd>실제 행정동은 분리되어 있으므로 만들 수 있습니다. 다만 1차에서는 대원 생활권으로 먼저 묶고, 유입이 생기면 대원1동·대원2동을 세부 페이지로 확장하는 것이 좋습니다.</dd>

    <dt id="faq-4">신장1동과 신장2동은 어떻게 처리하나요?</dt>
    <dd>1차에서는 신장 생활권으로 통합하고, 2차에서 신장1동과 신장2동을 나누는 방식이 좋습니다. 신장1동은 오산대역·수청동, 신장2동은 세교지구와 연결합니다.</dd>

    <dt id="faq-5">병점역이나 서동탄역도 오산 페이지로 만들어도 되나요?</dt>
    <dd>병점역과 서동탄역은 화성시 성격이 강하므로 오산에서는 인접 생활권으로만 설명하는 것이 좋습니다.</dd>
  </dl>
</section>
"""
}
