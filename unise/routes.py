import os
import time
from unise import app
from unise.indexbuilder import IndexBuilder
from unise.searcher import searcher
from flask import render_template, jsonify, request, send_from_directory
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
    limit = int(request.form['limit']) if request.form['limit'] != "" else 10

    mysearcher = searcher()
    res = mysearcher.search(keyword, "content", "subject", "year", sort_term=sort, hit_count=limit)

    return jsonify(res)


@app.route('/visual', methods=['POST'])
def visualize_pdf():
    path = request.form['path']
    filepath = os.getcwd().replace("\\", "/") + path.replace(".", "", 1)
    webbrowser.open_new(filepath)
    return filepath


@app.route('/create')
def create_page():
    return render_template('create.html')


@app.route('/build', methods=['POST'])
def build_index():
    if request.form['test'] == "test_data":
        test = True
    else:
        test = False

    try:
        builder = IndexBuilder()
        builder.create(test=test)
        return "200"
    except:
        return "error"



