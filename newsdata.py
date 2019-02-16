#!/usr/bin/env python3
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for
from newsdatadb import get_most_popular_three_articles, get_most_popular_author
from newsdatadb import get_date_when_error_test_failed

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB News</title>
    <style>
      h1, form, div, p { text-align: center; }
      form { border: 1px solid #999;
                   width: 600px;
                   margin-left: auto;
                   margin-right: auto;
                  }
    </style>
  </head>
  <body>
    <h1>DB News</h1>
    <form method="get" action="/article/top_three_articles">
      <div>
        1. What are the most popular three articles of all time?
        <button type="submit"> Check It Out! </button>
      </div>
    </form>
    <!-- result will go here -->
    <div>
%s
    </div>
    <form method="get" action="/article/best_authors">
      <div>
        2. Who are the most popular article authors of all time?
        <button type="submit"> Check It Out! </button>
      </div>
    </form>
    <!-- result will go here -->
    <div>
%s
    </div>
    <form method="get" action="/article/percentage_error">
      <div>
        3. On which days did more than 1 percentage of requests lead to errors?
        <button type="submit"> Check It Out! </button>
      </div>
    </form>
    <!-- result will go here -->
    <div>
%s
    </div>
  </body>
</html>
'''

# # HTML template for an individual comment
POST = '''\
  <p>"%s" -- %s views</p>
'''

POST2 = '''\
  <p>%s -- %s views</p>
'''

POST3 = '''\
  <p>%s -- %s errors</p>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    html = HTML_WRAP % ("", "", "")
    return html


@app.route('/article/top_three_articles', methods=['GET'])
def find_top_three_articles():
    '''desplays top three articles'''
    posts = "".join(
        POST % (title, sum) for title, sum in
        get_most_popular_three_articles()
    )
    html = HTML_WRAP % (posts, "", "")
    return html


@app.route('/article/best_authors', methods=['GET'])
def find_best_authors():
    '''displays the most popular authors in order'''
    posts = "".join(
        POST2 % (author, views) for author, views
        in get_most_popular_author()
    )
    html = HTML_WRAP % ("", posts, "")
    return html


@app.route('/article/percentage_error', methods=['GET'])
def find_errors():
    '''displays list of aritcle with percentage errors more than 1.0%'''
    posts = "".join(
        POST3 % (date, str(percentage_error) + '%') for date, percentage_error
        in get_date_when_error_test_failed()
    )
    html = HTML_WRAP % ("", "", posts)
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
