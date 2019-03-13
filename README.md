# Project Logs Analysis
### Solution by Adel KIHAL

This project is part of Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
## Project Objectives

Create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

It will mainly answer these three questions:

1. **What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
2. **Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. **On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Project Requirements
### System
- Linux
### Programs
1. python3 
3. postgresql
### Data
- database setup: [sql data file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## How to Run the Project
1. Extract the database
2. Use this command to load the data in postgresql ``` psql -d news -f newsdata.sql ```
3. Extract the project
4. Install the project dependancy ```pip3 install psycopg2-binary --user```
5. From within the project directory write in the terminal ```python3 catalog.py``` to run the project

### Project output 


    1. What are the most popular three articles of   all time?
    
    - Candidate is jerk, alleges rival -- 338647   views
    - Bears love berries, alleges bear -- 253801   views
    - Bad things gone, say good people -- 170098   views
    
    2. Who are the most popular article authors of   all time?
    
    - Ursula La Multa -- 507594 views
    - Rudolf von Treppenwitz -- 423457 views
    - Anonymous Contributor -- 170098 views
    - Markoff Chaney -- 84557 views
    
    3. On which days did more than 1%% of requests   lead to errors?
    
    - 2016-07-17 -- 1265 errors
