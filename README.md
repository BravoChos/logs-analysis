# Logs-Analysis
Project: Logs-Analysis

## About:
Sample Database API With postgresql database using psycopg2 module and simple web app.
The database contains authors, articles, and web server log for the site.
It will connect to that database and run the web server so the user can check the result of following 3 questions.

  1. What are the most popular three articles of all time? 
  Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

  Behavior:
	1. Request has to be HTTP localhost:8000/article/top_three_articles 
	2. Get sql result from postgresql by executing function get_most_popular_three_articles()	
	3. Put the sql result into HTML template which contains %s. 
	4. variable 'title' and 'sum' will be replaced with %s.
  Return:
  	Example:
  	"Princess Shellfish Marries Prince Handsome" — 1201 views
  	"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
  	"Political Scandal Ends In Political Scandal" — 553 views

  2. Who are the most popular article authors of all time? 
  That is, when you sum up all of the articles each author has written, which authors get the most page views? 
  Present this as a sorted list with the most popular author at the top.
  
  Behavior:
	1. Request has to be HTTP localhost:8000/article/top_three_articles 
	2. Get sql result from postgresql by executing function /article/best_authors()	
	3. Put the sql result into HTML template which contains %s. 
	4. variable 'author' and 'views' will be replaced with %s.
  Return:
	Example:
	Ursula La Multa — 2304 views
  	Rudolf von Treppenwitz — 1985 views
  	Markoff Chaney — 1723 views
  	Anonymous Contributor — 1023 views

  3. On which days did more than 1% of requests lead to errors? 
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.
  
  Behavior:
	1. Request has to be HTTP localhost:8000/article/top_three_articles 
	2. Get sql result from postgresql by executing function /article/percentage_error()	
	3. Put the sql result into HTML template which contains %s. 
	4. variable 'date' and 'error' will be replaced with %s.
  Return:
 	Example:
 	July 29, 2016 — 2.5% errors
  
## Steps to run the python codes:
	
  0. Setting up the Environment
  	1. Download and Install python3 ver 3.6.7 (https://www.python.org/downloads/)
	2. Install Vagrant Tools to turn on Virtual Machine ( https://www.vagrantup.com/downloads.html )
	3. Install VirtualBox Version 5.1.38 r122592 (https://www.virtualbox.org/wiki/Downloads)
	4. Download the VM configuration called FSND-Virtual-Machine for this project ( https://github.com/udacity/fullstack-nanodegree-vm ) 
  	5. Download the database file called 'newsdata.sql'
	(https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
	6. Put it into vagrant directory which is shared with your virtual machine
	7. To load the data, cd into vagrant directory use the following command
		1) vargran up 
		2) vagrant ssh
		3) psql -d news -f newsdata.sql

  1. clone the repository into vagrant directory from the following source.
	(https://github.com/DeepLearnerSC/Project-Logs-Analysis)
  2. 'cd' to 'Log-Analysis' and you will find 'newsdata.py' and 'newsdatadb.py'
  3. Command Vagrant up, ans then type Vagrant SSH to start the VM
  2. Command python newsdata.py, then you are ready to test the 'Log-Analysis'
  3. Open up your browser and go to http://0.0.0.0:8000.
  4. click the 'check it out' button to see the result of every each one of three questions.

##PSQL Command Used To create the view
1. get_most_popular_three_articles
'''
SELECT authors.name AS author, count(log.path) AS views
FROM articles, authors, log
WHERE authors.id = articles.author
AND log.path = concat('/article/', articles.slug)
GROUP BY authors.name
ORDER BY views desc
      '''

2. get_date_when_error_test_failed
'''
SELECT authors.name AS author, count(log.path) AS views
FROM articles, authors, log
WHERE authors.id = articles.author
AND log.path = concat('/article/', articles.slug)
GROUP BY authors.name
ORDER BY views desc
'''

3. get_date_when_error_test_failed
'''
SELECT
  to_char(errorTest.date, 'Mon DD, YYYY'),
  ROUND(errorTest.percentage_error, 2)
FROM (
  SELECT status_error.date AS date, 
    CAST((SUM(status_error.errors))/(SUM(status_total.total)) * 100
    AS numeric) AS percentage_error
  FROM (
    SELECT date(time) AS date, count(status) AS errors
    FROM log
    WHERE status
    LIKE '404%'
    GROUP BY date
  ) AS status_error
  JOIN (
    SELECT date(time) AS date, count(status) AS total
    FROM log
    GROUP BY date
  ) AS status_total
  ON status_error.date = status_total.date
  GROUP BY status_error.date
) AS errorTest
WHERE errorTest.percentage_error > 1.0
'''
	
