# 오산시 출장마사지 사이트 공통 설정

BASE_URL = "https://osan-massage1.pages.dev"

BRAND = "바로 GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 사이트 루트 경로 — 오산은 행정구가 없으므로 구별 페이지를 만들지 않는다.
HOME = "/gyeonggi/osan/"

# 문의 채널 (텔레그램)
TELEGRAM = "https://t.me/googleseolab"

# 상단 메뉴 — 키워드 반복 없음, 지역명·역명만 표시 (메뉴명에 "출장마사지" 미사용)
NAV = [
    ("오산 홈", "/gyeonggi/osan/", []),
    ("지역별 안내", "/gyeonggi/osan/", [
        ("중앙동", "/gyeonggi/osan/jungang-dong/"),
        ("대원 생활권", "/gyeonggi/osan/daewon-area/"),
        ("대원1동", "/gyeonggi/osan/daewon-1-dong/"),
        ("대원2동", "/gyeonggi/osan/daewon-2-dong/"),
        ("남촌동", "/gyeonggi/osan/namchon-dong/"),
        ("신장 생활권", "/gyeonggi/osan/sinjang-area/"),
        ("신장1동", "/gyeonggi/osan/sinjang-1-dong/"),
        ("신장2동", "/gyeonggi/osan/sinjang-2-dong/"),
        ("세마동", "/gyeonggi/osan/sema-dong/"),
        ("초평동", "/gyeonggi/osan/chopyeong-dong/"),
    ]),
    ("역세권 안내", "/gyeonggi/osan/", [
        ("오산역", "/gyeonggi/osan/station/osan-station/"),
        ("오산대역", "/gyeonggi/osan/station/osandae-station/"),
        ("세마역", "/gyeonggi/osan/station/sema-station/"),
        ("병점역 인접", "/gyeonggi/osan/station/byeongjeom-nearby-area/"),
        ("서동탄역 인접", "/gyeonggi/osan/station/seodongtan-nearby-area/"),
        ("진위역 인접", "/gyeonggi/osan/station/jinwi-nearby-area/"),
    ]),
    ("생활권 안내", "/gyeonggi/osan/", [
        ("오산역·중앙동", "/gyeonggi/osan/area/osan-station-jungang/"),
        ("오산대역·수청동", "/gyeonggi/osan/area/osandae-sucheong/"),
        ("세마역·세마동", "/gyeonggi/osan/area/sema-dong/"),
        ("세교신도시", "/gyeonggi/osan/area/segyeo-newtown/"),
        ("대원·원동", "/gyeonggi/osan/area/daewon-won-dong/"),
        ("남촌·궐동", "/gyeonggi/osan/area/namchon-gwol-dong/"),
        ("신장·수청", "/gyeonggi/osan/area/sinjang-sucheong/"),
        ("초평·가장동", "/gyeonggi/osan/area/chopyeong-gajang/"),
        ("갈곶·고현", "/gyeonggi/osan/area/galgot-gohyeon/"),
        ("오산 IC·물류", "/gyeonggi/osan/area/osan-ic-logistics/"),
    ]),
    ("예약 안내", "/gyeonggi/osan/reservation/", []),
    ("이용 전 확인사항", "/gyeonggi/osan/check/", []),
    ("홈타이 이용 가이드", "/gyeonggi/osan/guide/", []),
    ("고객센터", "/gyeonggi/osan/support/", [
        ("개인정보처리방침", "/gyeonggi/osan/support/privacy/"),
    ]),
]
