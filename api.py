# http://localhost:90/users

from db import get_users

from flask import Flask
from flask_cors import cross_origin
from flask import jsonify
from waitress import serve



app = Flask(
    __name__,
    template_folder='build',
    static_folder='build'
)


@app.route('/users', strict_slashes=False)
@cross_origin()
def main_page() -> str:
    users = get_users()
    return jsonify(users)

if __name__ == '__main__':
    # serve(app, port=90, host='0.0.0.0')
    app.run(host='0.0.0.0')
