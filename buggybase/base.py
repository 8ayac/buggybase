import random
from base64 import b64decode, b64encode

from flask import abort, redirect, render_template, render_template_string, request, url_for
from flask import Blueprint

bp = Blueprint('base', __name__)


@bp.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')


@bp.route('/', methods=['POST'])
def post_index():
    mode = request.form['mode']
    if mode not in ['encode', 'decode']:
        return redirect(url_for('/'))

    s = request.form['s']
    ret_s = encode(s) if mode == 'encode' else decode(s)
    return render_template('index.html', result=ret_s)


@bp.errorhandler(500)
def internal_server_error(e):
    mascot = random.choice(list('🐌🐛🦟🐜🐝🐞🦂🦗🦋🕷'))  # just choose a mascot
    return render_template_string(f'{mascot}&lt; {e.description}')


def encode(s: str):
    return b64encode(s.encode()).decode('utf-8')


def decode(s: str):
    try:
        result = b64decode(s.encode()).decode('utf-8')
    except:
        abort(500, description=f'base64: invalid input ({s=})')

    return result
