from unise import app
from unise.searcher import searcher
from flask import render_template, jsonify, request
import webbrowser


@app.route('/')
@app.route('/index')
def index():

    '''mysearcher = searcher()
    res = mysearcher.search("analisi sistemica", "content", "subject")
    x = res[0]
    print(x)
    return ""+str(res[0])
    '''
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def process():
    keyword = request.form['keyword']
    sort = request.form['sort']

    mysearcher = searcher()
    res = mysearcher.search(keyword, "content", "subject", "year", sort_term=sort)

    return jsonify(res)


@app.route('/visual', methods=['POST'])
def visualize_pdf():
    return ""

