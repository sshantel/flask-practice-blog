from flask import Flask, render_template
from forms import SignUpForm

app = Flask(__name__) #create Flask application
app.config['SECRET_KEY'] = 'supersecret'

@app.route('/') #create route in server that's a single slash
def home():
    return 'Hello World'

@app.route('/blog')
def blog():
    posts = [{'title': 'Cooking Ramen', 'author': 'Chantel'},
             {'title': 'Buying Sushi', 'author': 'Chantel'}]
    return render_template('blog.html', author="Chantel", cooking=False, posts=posts)

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')