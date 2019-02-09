# Logs-Analysis
Project: Logs-Analysis

## About:
Sample Database API With postgresql database using psycopg2 module
The database contains authors, articles, and web server log for the site.
It will connect to that database and run the web server so the user can check the result of following 3 questions.

  1. What are the most popular three articles of all time? 
  Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

  Example:
  "Princess Shellfish Marries Prince Handsome" — 1201 views
  
  "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
  
  "Political Scandal Ends In Political Scandal" — 553 views

  2. Who are the most popular article authors of all time? 
  That is, when you sum up all of the articles each author has written, which authors get the most page views? 
  Present this as a sorted list with the most popular author at the top.

  Example:
  Ursula La Multa — 2304 views
  
  Rudolf von Treppenwitz — 1985 views
  
  Markoff Chaney — 1723 views
  
  Anonymous Contributor — 1023 views

  3. On which days did more than 1% of requests lead to errors? 
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

  Example:
  July 29, 2016 — 2.5% errors
  
## Steps to run the python codes:

  0. Setting the VM and download the database file (please check the instuction from fullstack nanodegree )
	1. cd to FSND-Virtual-Machine Directory and Type Vagrant up, ans then type Vagrant SSH
  2. command python newsdata.py 
  3. open up the browser and go to http://0.0.0.0:8000
  4. click the 'check it out' button to see the result of every each one of three questions.

	
