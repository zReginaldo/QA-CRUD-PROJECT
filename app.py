# imports app object from ./application/__init__.py
from application import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
