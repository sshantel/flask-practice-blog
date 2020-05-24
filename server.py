from flask import Flask, render_template

app = Flask(__name__) #create Flask application

@app.route('/') #create route in server that's a single slash
def home():
    return 'Hello World'

@app.route('/blog')
def blog():
    return render_template('blog.html', author="Chantel", cooking=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')