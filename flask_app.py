from flask import Flask, render_template, request, jsonify
import sqlite3
import os
import requests
import schedule, time
from bs4 import BeautifulSoup


# 절대 경로를 사용해야지 호스팅에서 경로를 읽을 수 있다
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "myblog.db")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 페이지 번호 가져오기 (기본값은 1)
    page = int(request.args.get('page', 1))
    items_per_page = 10
    offset = (page - 1) * items_per_page

    # 검색어 가져오기 (기본값은 빈 문자열)
    search_term = request.args.get('keyword', "")

    # 총 검색 결과 개수 조회
    cursor.execute("SELECT COUNT(*) FROM blog WHERE title LIKE ? OR summary LIKE ?", 
                   ('%' + search_term + '%', '%' + search_term + '%'))
    total_results = cursor.fetchone()[0]
    total_pages = (total_results + items_per_page - 1) // items_per_page

    # 검색어를 포함하는 title 또는 summary를 가진 레코드 검색
    cursor.execute("SELECT * FROM blog WHERE title LIKE ? OR summary LIKE ? ORDER BY date DESC LIMIT ? OFFSET ?", 
                   ('%' + search_term + '%', '%' + search_term + '%', items_per_page, offset))
    
    blog_data = cursor.fetchall()

    # 연결 종료
    conn.close()

    return render_template('index.html', blog_data=blog_data, current_page=page, total_pages=total_pages, keyword=search_term)

@app.route('/dynamic', methods=['GET'])
def dynamic():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # 커서가 반환하는 행을 딕셔너리처럼 접근할 수 있도록 설정합니다.
    cursor = conn.cursor()

    # 페이지 번호 가져오기 (기본값은 1)
    page = int(request.args.get('page', 1))
    items_per_page = 10
    offset = (page - 1) * items_per_page

    # 검색어 가져오기 (기본값은 빈 문자열)
    search_term = request.args.get('keyword', "")

    # 총 검색 결과 개수 조회
    cursor.execute("SELECT COUNT(*) FROM blog WHERE title LIKE ? OR summary LIKE ?", 
                   ('%' + search_term + '%', '%' + search_term + '%'))
    total_results = cursor.fetchone()[0]
    total_pages = (total_results + items_per_page - 1) // items_per_page

    # 검색어를 포함하는 title 또는 summary를 가진 레코드 검색
    cursor.execute("SELECT * FROM blog WHERE title LIKE ? OR summary LIKE ? ORDER BY date DESC LIMIT ? OFFSET ?", 
                   ('%' + search_term + '%', '%' + search_term + '%', items_per_page, offset))
    
    # fetchall() 호출 결과를 딕셔너리 리스트로 변환합니다.
    blog_data = [dict(row) for row in cursor.fetchall()]
    print(blog_data)

    # 연결 종료
    conn.close()

    # 검색 결과와 페이지 정보를 JSON으로 반환
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Flask에서는 request.is_xhr로 AJAX 요청을 확인할 수 있습니다.
        return jsonify({
            'blog_data': blog_data,
            'total_pages': total_pages,
            'current_page': page
        })
    else:
        return render_template('dynamic_page.html', blog_data=blog_data, current_page=page, total_pages=total_pages, keyword=search_term)

# 나머지 코드


# @app.route('/crawling', methods=['GET'])
# def schedule_set():
#     schedule.every(10).seconds.do(crawling)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# def crawling():
#     response = requests.get("https://www.vans.co.kr/category/men/allshoes")
#     soup = BeautifulSoup(response.text, 'html.parser')
#     items = soup.select(".plp-grid-item")
#     for item in items:
#         name = item.select_one(".text-link").text
#         print(name)


if __name__ == '__main__':
    app.run(debug=True)