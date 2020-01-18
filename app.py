#!flask/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': u'Fortaleza Digital',
        'author': u'Dan Brow',
        'edition': '1 edicção'
    },
    {
        'id': 2,
        'title': u'Live do Python',
        'author': u'Eduardo',
        'edition': ''
    }
]


@app.route('/library/api/v1.0/books', methods=['GET'])
def get_all_books():
    return jsonify({'books': books})


@app.route('/library/api/v1.0/books/<int:book_id>', methods=['GET'])
def get_uniq_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        return jsonify({'book_not_found': 'This book is not in our store'})
    return jsonify({'book': book[0]})


@app.route('/library/api/v1.0/books/', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json.get('author', ""),
        'edition': request.json.get('edition', "")
    }
    books.append(book)
    return jsonify({'book_created': book}), 201


@app.route('/library/api/v1.0/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        return jsonify({'book_not_found': 'This book is not in our store'})
    book[0]['title'] = request.json.get('title', book[0]['title'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    book[0]['edition'] = request.json.get('edition', book[0]['edition'])
    return jsonify({'book_updated': book[0]})


@app.route('/library/api/v1.0/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        return jsonify({'book_not_found': 'This book is not in our store'})
    books.remove(book[0])
    return jsonify({'book_deleted': book[0]})


if __name__ == '__main__':
    app.run(debug=True)