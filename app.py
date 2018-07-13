from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def verification():
    return render_template('verification.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')