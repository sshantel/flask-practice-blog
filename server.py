from flask import Flask, render_template, redirect, request
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

@app.route('/signup', methods =['GET','POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')