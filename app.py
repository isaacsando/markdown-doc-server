import markdown
import os

from flask import Flask, render_template

DOCS_ROOT = 'docs'

app = Flask(__name__)

def _build_docs_list():
    docs = {d: _get_docs_by_dir(d) for d in _get_doc_dirs()}
    return docs

def _get_doc_dirs():
    return os.listdir(DOCS_ROOT)

def _get_docs_by_dir(dir_name):
    return os.listdir(os.path.join(DOCS_ROOT, dir_name))

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
    app.run(host='0.0.0.0', port=8888, debug=True)
