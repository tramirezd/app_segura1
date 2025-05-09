from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app, content_security_policy={'default-src': ["'self'"]})

@app.route('/')
def index():
    return '¡Hola, mi nombre es Tania Ramirez'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
