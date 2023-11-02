import sqlite3

# SQLite 데이터베이스 연결
conn = sqlite3.connect('myblog.db')
cursor = conn.cursor()

import random

additional_posts = [
    {
        "title": "AI와 예술의 만남",
        "category": "인공 지능",
        "date": "2025-01-15",
        "summary": "인공 지능과 예술이 만나면 어떤 놀라운 예술작품이 탄생할까요? 이번 글에서는 AI 예술의 현재와 미래에 대해 다룹니다. 예술가와 AI의 협력으로 세상을 더 아름답게 만들어보세요.",
        "views": random.randint(1000, 5000),
        "likes": random.randint(50, 300)
    },
    {
        "title": "스마트 시티의 미래",
        "category": "스마트 시티",
        "date": "2025-02-05",
        "summary": "스마트 시티가 현실화되면 도시생활은 어떻게 바뀔까요? 미래 도시에 대한 상상을 펼쳐보며 스마트 시티의 가능성을 탐색합니다. 지속 가능하고 효율적인 도시를 위한 기술 혁신을 살펴봅시다.",
        "views": random.randint(1000, 5000),
        "likes": random.randint(50, 300)
    },
    {
        "title": "사용자 중심의 웹 디자인",
        "category": "웹 디자인",
        "date": "2025-02-20",
        "summary": "웹 디자인에서 사용자 중심의 접근 방식은 왜 중요한 것일까요? 사용자 경험을 개선하고 웹 사이트의 효율성을 높이는 웹 디자인 원칙을 살펴봅시다. 사용자를 고려한 웹 디자인의 예시를 소개합니다.",
        "views": random.randint(1000, 5000),
        "likes": random.randint(50, 300)
    },
    {
        "title": "양자 컴퓨팅의 미래",
        "category": "양자 컴퓨팅",
        "date": "2025-03-10",
        "summary": "양자 컴퓨팅 기술은 어떻게 우리의 일상과 비즈니스에 혁신을 가져올 수 있을까요? 양자 컴퓨팅의 작동 원리와 가능한 응용 분야를 탐색합니다. 양자 컴퓨터가 복잡한 문제를 해결하는 방법을 알아보세요.",
        "views": random.randint(1000, 5000),
        "likes": random.randint(50, 300)
    },
    {
        "title": "생활 속의 로봇 기술",
        "category": "로봇 공학",
        "date": "2025-03-25",
        "summary": "로봇 기술이 일상생활에 어떻게 적용되고 있는지 살펴봅니다. 로봇 가정부부터 의료 분야까지 로봇 기술의 다양한 활용 사례를 소개합니다. 로봇의 미래 가능성을 엿봅시다.",
        "views": random.randint(1000, 5000),
        "likes": random.randint(50, 300)
    },
    {
        "title": "사이버 보안의 최신 동향",
        "category": "사이버 보안",
        "date": "2025-04-10",
        "summary": "사이버 보안 분야에서 발생한 최신 이슈와 트렌드를 살펴봅니다. 사이버 공격과 방어에 대한 최신 정보를 제공하며, 개인과 기업의 보안을 강화하는 방법을 탐색합니다.",
        "views": random.randint(1000, 5000),
        "likes": random.randint(50, 300)
    },
    {
        "title": "데이터 과학의 미래",
        "category": "데이터 과학",
        "date": "2025-04-25",
        "summary": "데이터 과학 분야의 발전과 예상되는 미래 동향을 살펴봅니다. 데이터 분석과 기계 학습의 혁신적인 응용 사례를 소개하며, 데이터 과학자의 역할과 중요성을 강조합니다.",
        "views": random.randint(1000, 5000),
        "likes": random.randint(50, 300)
    },
    {
        "title": "AR과 VR의 혁신",
        "category": "증강 현실/가상 현실",
        "date": "2025-05-10",
        "summary": "증강 현실(AR)과 가상 현실(VR) 기술의 혁신과 활용 사례를 살펴봅니다. 실시간 3D 체험부터 교육과 엔터테인먼트까지 다양한 분야에서 AR과 VR 기술이 혁신을 이끌어내는 모습을 확인하세요.",
        "views": random.randint(1000, 5000),
        "likes": random.randint(50, 300)
    },
    {
        "title": "퀀텀 인터넷의 미래",
        "category": "퀀텀 인터넷",
        "date": "2025-05-25",
        "summary": "퀀텀 인터넷의 개발과 전세계적인 네트워크 변화에 대한 전망을 살펴봅니다. 정보 보안과 통신의 혁신을 이끄는 퀀텀 인터넷 기술을 탐구하며, 디지털 세계의 미래를 그려봅시다.",
        "views": random.randint(1000, 5000),
        "likes": random.randint(50, 300)
    },
    {
        "title": "자율 주행차의 현실화",
        "category": "자율 주행",
        "date": "2025-06-10",
        "summary": "자율 주행차 기술의 발전과 도로에서의 현실 적용 가능성을 탐색합니다. 자동차 산업의 혁신과 교통 시스템의 변화에 대해 알아보며, 자율 주행차의 미래에 대한 기대를 공유합니다.",
        "views": random.randint(1000, 5000),
        "likes": random.randint(50, 300)
    },
    {
        "title": "로봇 가정부의 시대",
        "category": "로봇 공학",
        "date": "2025-06-25",
        "summary": "로봇 가정부와 인공 지능이 가정 생활에 어떻게 도움을 주는지 살펴봅니다. 스마트 홈과 로봇 도우미의 혁신을 탐구하며, 로봇 기술이 일상의 부담을 덜어내는 방법을 소개합니다.",
        "views": random.randint(1000, 5000),
        "likes": random.randint(50, 300)
    },
    # 나머지 10개 데이터는 위와 같은 형식으로 생성
]



# 블로그 게시물 데이터를 데이터베이스에 입력
for post in additional_posts:
    cursor.execute("INSERT INTO blog (title, category, date, summary, views, likes) VALUES (?, ?, ?, ?, ?, ?)", (post["title"], post["category"], post["date"], post["summary"], post["views"], post["likes"]))

# 테이블에 변경 내용 저장
conn.commit()

# 연결 종료
conn.close()