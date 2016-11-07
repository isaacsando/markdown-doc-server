import glob
import markdown
import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

DOCS_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs')
HOST = '0.0.0.0'
PORT = 8888

def _create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = _create_app()

def _build_docs_list():
    docs = {d: _get_docs_by_dir(d) for d in _get_doc_dirs()}
    return docs

def _get_doc_dirs():
    try:
        return os.listdir(DOCS_ROOT)
    except FileNotFoundError as err:
        msg = ('{0} was not found. Please ensure the DOCS_ROOT variable is a '
               'valid path.'
              ).format(DOCS_ROOT)
        raise Exception(msg) from err

def _get_docs_by_dir(dir_name):
    # return only .md files
    return [os.path.basename(f)
            for f in glob.glob(os.path.join(DOCS_ROOT, dir_name, '*.md'))]

def _get_html_from_md(doc_type, md_file):
    doc_file = os.path.join(DOCS_ROOT, doc_type, md_file)

    with open(doc_file) as f:
        html = markdown.markdown(
            f.read(),
            extensions=[
                'markdown.extensions.tables',
                'markdown.extensions.fenced_code'
                ])
        return html

@app.context_processor
def inject_md_folders():
    return dict(docs=_build_docs_list())

@app.route("/")
def index():
    docs = _build_docs_list()
    return render_template('index.html', docs=docs)

@app.route("/docs/<doc_type>/<md_file>")
def md_installs(doc_type, md_file):
    doc_html = _get_html_from_md(doc_type, md_file)
    return render_template('base_md_files.html', doc_html=doc_html)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=str(e)), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', e=str(e)), 500

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
