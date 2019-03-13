#!/bin/pyhton3

import psycopg2

'''
File: catalog.py
Created by Adel KIHAL
Date: 2019-03-13
Description: This program is a solution of the udacity fsnd first project
             Log Analysis
Requirements: psycopg2
            python2: pip install psycopg2-binary --user
            python3: pip3 install psycopg2-binary --user

'''


'''Function that access the database to get top articles
Which articles have been accessed the most? Present this
information as a sorted list with the most popular article at the top.
Returns:
    list of tuples or none -- result of the query
'''


def top_articles():
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    query = '''
SELECT title,
       Count(slug) AS visits
FROM   articles
       LEFT JOIN log
              ON articles.slug = Split_part(log.path, '/', 3)
GROUP  BY title
ORDER  BY visits DESC
LIMIT  3;
    '''
    cur.execute(query)
    res = cur.fetchall()
    conn.close()
    return res


'''Function that access the database to get top authors
That is, when you sum up all of the articles each
author has written, which authors get the most page views?
Present this as a sorted list with the most popular author at the top.
Returns:
    list of tuples or none -- result of the query
'''


def top_authors():
    conn = psycopg2.connect('dbname=news')
    cur = conn.cursor()
    query = '''
SELECT name,
       Count(slug) AS visits
FROM   authors,
       articles,
       log
WHERE  authors.id = articles.author
       AND articles.slug = Split_part(log.path, '/', 3)
GROUP  BY name
ORDER  BY visits DESC;
    '''
    cur.execute(query)
    res = cur.fetchall()
    conn.close()
    return res


'''Function that access the database to get access errors above 1%
The log table includes a column status that indicates
the HTTP status code that the news site sent to the user's browser.
Returns:
    list of tuples or none -- result of the query
'''


def log_errors():
    conn = psycopg2.connect('dbname=news')
    cur = conn.cursor()
    query = '''
SELECT   TIME::DATE AS date1,
  Count(status) filter (WHERE status LIKE '%40%') AS errors,
  count(status) AS total,
  count(status) filter (WHERE status LIKE '%40%') *100.0 / count(status)
  AS percentage
FROM     log
GROUP BY date1
HAVING count(status) filter (WHERE status LIKE '%40%')*100.0/count(status)>1.0
ORDER BY date1 ASC;
    '''
    cur.execute(query)
    res = cur.fetchall()
    conn.close()
    return res


'''[Functions to display the result of a query in the terminal]
'''


def print_top_articles(res):
    print("\n1. What are the most popular three articles of all time?\n")
    for article in res:
        print("- %s -- %d views" % (article[0], article[1]))


def print_top_authors(res):
    print("\n2. Who are the most popular article authors of all time?\n")
    for author in res:
        print("- %s -- %d views" % (author[0], author[1]))


def print_log_errors(res):
    print("\n3. On which days did more than 1%% of requests lead to errors?\n")
    for error in res:
        print("- %s -- %d errors" % (error[0], error[1]))


print_top_articles(top_articles())
print_top_authors(top_authors())
print_log_errors(log_errors())
