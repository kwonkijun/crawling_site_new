import sqlite3

# SQLite 데이터베이스 연결
conn = sqlite3.connect('myblog.db')
cursor = conn.cursor()

# 블로그 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS blog (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  category TEXT,
                  title TEXT,
                  date TEXT,
                  summary TEXT,
                  views INTEGER,
                  likes INTEGER)''')

# 테이블에 변경 내용 저장
conn.commit()

additional_posts = [
    {
        "title": "게임 업계에서의 블록체인 혁명!",
        "category": "블록체인",
        "date": "2024-07-05",
        "summary": "블록체인이 게임 산업을 어떻게 변화시키고 있는지 깊이 파헤쳐봅시다.",
        "views": 4500,
        "likes": 200
    },
    {
        "title": "VR로 체험하는 우주여행!",
        "category": "혼합 현실",
        "date": "2024-07-12",
        "summary": "우주를 가볼 필요 없이, VR 기술로 집에서 우주를 탐험해 보세요!",
        "views": 4800,
        "likes": 240
    },
    {
        "title": "클라우드 게임의 혁신적 진화",
        "category": "클라우드",
        "date": "2024-07-20",
        "summary": "게임을 다운로드 할 필요 없이 클라우드에서 즉시 게임을 즐겨보세요!",
        "views": 5200,
        "likes": 260
    },
    {
        "title": "AI로 창작된 음악의 세계",
        "category": "인공 지능",
        "date": "2024-07-28",
        "summary": "인공 지능이 창작한 음악, 그 안에서 찾아낼 수 있는 새로운 감동을 경험해보세요.",
        "views": 4900,
        "likes": 230
    },
    {
        "title": "스마트홈 보안 위협! 어떻게 대비할 것인가?",
        "category": "사이버 보안",
        "date": "2024-08-05",
        "summary": "사이버 공격자들의 새로운 타겟이 되고 있는 스마트홈! 이를 방어하기 위한 최신 전략은?",
        "views": 4100,
        "likes": 210
    },
    {
        "title": "6G의 세계, 우리를 기다리는 놀라운 미래",
        "category": "5G",
        "date": "2024-08-15",
        "summary": "5G보다 더 빠르고, 더 넓은 세계! 6G의 가능성을 함께 탐구해보세요.",
        "views": 4600,
        "likes": 250
    },
    {
        "title": "블록체인과 금융, 새로운 가능성을 창출하다",
        "category": "블록체인",
        "date": "2024-08-25",
        "summary": "블록체인 기술이 금융 산업에 가져올 변화와 혁신에 대해 깊이 있게 알아보자.",
        "views": 4200,
        "likes": 210
    },
    {
        "title": "IoT 기술, 생활을 더 편리하게!",
        "category": "IoT",
        "date": "2024-09-05",
        "summary": "IoT의 최신 기술 동향과 그로 인해 변화하게 될 우리의 생활에 대해 알아보세요.",
        "views": 4300,
        "likes": 220
    },
    {
        "title": "로봇 공학의 현재와 미래",
        "category": "로봇 공학",
        "date": "2024-09-15",
        "summary": "로봇 공학이 우리 생활에 가져올 긍정적인 영향과 함께 향후 기대되는 기술들에 대해 알아보자.",
        "views": 4100,
        "likes": 205
    },
    {
        "title": "데이터 과학자가 되기 위한 첫 걸음",
        "category": "데이터 과학",
        "date": "2024-09-25",
        "summary": "데이터 과학자의 역할과 함께 어떻게 그 길을 걷기 시작할 수 있는지 깊이 있는 가이드를 제공합니다.",
        "views": 5000,
        "likes": 240
    },
    {
        "title": "딥 러닝의 세계, 무엇을 할 수 있을까?",
        "category": "인공 지능",
        "date": "2024-10-05",
        "summary": "딥 러닝 기술의 기초부터 응용까지, 그 흥미진진한 세계를 함께 탐험해보세요.",
        "views": 4800,
        "likes": 235
    },
    {
        "title": "AR의 무한한 가능성 탐구",
        "category": "혼합 현실",
        "date": "2024-10-15",
        "summary": "증강 현실(AR)이 현실 세계와 가상의 세계를 어떻게 접목시키고 있는지 알아보세요.",
        "views": 4700,
        "likes": 225
    },
    {
        "title": "퀀텀 컴퓨터의 세계로!",
        "category": "퀀텀 컴퓨팅",
        "date": "2024-10-25",
        "summary": "퀀텀 컴퓨팅의 기본 원리와 그로 인해 열리게 될 새로운 가능성들을 함께 탐색해보자.",
        "views": 4400,
        "likes": 215
    },
    {
        "title": "5G 기술의 활용 사례들",
        "category": "5G",
        "date": "2024-11-05",
        "summary": "5G 기술을 활용하여 어떤 서비스와 제품들이 탄생하고 있는지 살펴봅니다.",
        "views": 4500,
        "likes": 220
    },
    {
        "title": "자율주행 차량, 도로 위의 미래",
        "category": "자율주행",
        "date": "2024-11-15",
        "summary": "자율주행 기술의 최신 동향과 함께 도로 위에서 만날 수 있는 미래에 대해 알아보세요.",
        "views": 4600,
        "likes": 230
    },
    {
        "title": "사이버 보안, 해킹을 막는 기술",
        "category": "사이버 보안",
        "date": "2024-11-25",
        "summary": "사이버 공격에 대한 방어 전략과 함께 새로운 보안 기술의 등장에 대해 알아보자.",
        "views": 4200,
        "likes": 210
    },
    {
        "title": "클라우드 기술의 무한한 확장성",
        "category": "클라우드",
        "date": "2024-12-05",
        "summary": "클라우드 기술의 발전과 그로 인한 산업의 변화를 깊이 있게 살펴보세요.",
        "views": 4300,
        "likes": 215
    },
    {
        "title": "가상 현실, 더 진짜 같은 체험을 위하여",
        "category": "혼합 현실",
        "date": "2024-12-15",
        "summary": "가상 현실 기술의 진화와 그로 인해 가능해지는 새로운 체험들을 알아보세요.",
        "views": 4400,
        "likes": 220
    },
    {
        "title": "AI와 함께하는 스마트 시티의 미래",
        "category": "인공 지능",
        "date": "2024-12-25",
        "summary": "스마트 시티 구축을 위한 인공 지능의 역할과 기술에 대해 깊이 있게 탐구해봅니다.",
        "views": 4700,
        "likes": 225
    },
    {
        "title": "바이오 테크, 인간의 미래를 위한 기술",
        "category": "바이오 테크",
        "date": "2024-12-30",
        "summary": "바이오 테크의 발전과 함께 인간의 건강과 미래에 미치는 영향에 대해 알아보자.",
        "views": 4600,
        "likes": 230
    }
]

# 블로그 게시물 데이터를 데이터베이스에 입력
for post in additional_posts:
    cursor.execute("INSERT INTO blog (title, category, date, summary, views, likes) VALUES (?, ?, ?, ?, ?, ?)", (post["title"], post["category"], post["date"], post["summary"], post["views"], post["likes"]))

# 테이블에 변경 내용 저장
conn.commit()

# 연결 종료
conn.close()