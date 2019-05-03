from flask import Flask

app = Flask(__name__)

def wrap_html(message):
    html = """
        <html>
        <body>
            <div style='font-size:120px;'>
            <center>
                <image height="200" width="800" src="http://pluspng.com/img-png/python-logo-png-newpythonlogo-png-1024.png">
                <br>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(message)
    return html

@app.route('/')
def hello_world():
    message = 'Welcome to the DevOps Project!'
    html = wrap_html(message)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)