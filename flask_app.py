from flask import Flask, render_template, request
import sqlite3
import os

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

if __name__ == '__main__':
    app.run(debug=True)