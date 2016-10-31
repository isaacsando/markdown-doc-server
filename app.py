import glob
import markdown
import os

from flask import Flask, render_template

DOCS_ROOT = os.path.join(os.path.dirname(__file__), 'docs')
HOST = '0.0.0.0'
PORT = 8888

app = Flask(__name__)

def _build_docs_list():
    docs = {d: _get_docs_by_dir(d) for d in _get_doc_dirs()}
    return docs

def _get_doc_dirs():
    return os.listdir(DOCS_ROOT)

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

@app.route("/")
def index():
    docs = _build_docs_list()
    return render_template('index.html', docs=docs)

@app.route("/docs/<doc_type>/<md_file>")
def md_installs(doc_type, md_file):
    return _get_html_from_md(doc_type, md_file)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
