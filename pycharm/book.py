from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
	# 1. 클라이언트가 준 title, author, review 가져오기.
    print(request.form['title'], ":", request.form['author'], ":", request.form['review'])
    book_title = request.form['title']
    book_author = request.form['author']
    book_review = request.form['review']
	# 2. DB에 정보 삽입하기
    doc = {
        'title': book_title,
        'author': book_author,
        'review': book_review
    }
    db.book.insert_one(doc)
    #db.변수명.insert_one(doc)
	# 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})

@app.route('/reviews', methods=['GET'])
def read_reviews():
    send_data = []
    book_all_reviews = list(db.book.find())
    for review in book_all_reviews:
        send_data.append({
            'title' : review['title'],
            'author' : review['author'],
            'review' : review['review']
        })
    return jsonify({'result': 'success', 'data': send_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)