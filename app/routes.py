from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username':'dhir4j'}
    title = "Home - Microblog"
    posts = [
        {   
            'author': {'username':'John'},
            'body':'Beautiful day in Poland!'
        },
        {   
            'author': {'username':'Mac'},
            'body':'The GodFather movie was cool!'
        }
    ]
    return render_template('index.html', user=user, title=title, posts=posts)
    