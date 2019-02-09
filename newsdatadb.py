# "Database code" for the DB News.

import psycopg2, bleach

DBNAME = "news"

def get_most_popular_three_articles():
  """Return most popluar three articles from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select path, count(*) as sum from log WHERE log.path != '/' GROUP BY path ORDER BY sum desc limit 3")
  result = c.fetchall()
  db.close()
  return result

def get_most_popular_author():
  """Return most popluar article author of all time from the 'database' """
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(
    """
    select authors.name as author, count(log.path) as views 
    from articles, authors, log 
    WHERE authors.id = articles.author and log.path LIKE concat('%', articles.slug,'%') 
    GROUP BY authors.name ORDER BY views desc
    """
  ) 
  result = c.fetchall()
  db.close()
  return result

def get_date_when_error_test_failed():
  """Return days where more than 1% of requests lead to errors from the 'database' """
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(
    """
    select t.date, t.percentage_error 
    from (select status_error.date as date, cast( (sum(status_error.errors))/(sum(status_error.errors)+sum(status_ok.ok))*100 as numeric) as percentage_error
      from (select date(time) as date, count(status) as errors from log where status LIKE '404%' GROUP BY date) as status_error 
    JOIN (select date(time) as date, count(status) as ok  from log where status LIKE '200%' GROUP BY date) as status_ok 
    ON status_error.date = status_ok.date    
    group by status_error.date ) as t WHERE t.percentage_error > 1.0
    """)
  result = c.fetchall()
  db.close()
  return result
