# Logs Analysis Project

This Project is creating a tool which is analysing the news database which consists of Authors, Articles and Logs and prints the report after analysing.

## Modules
* logsanalysis.py
* newsdata.sql

### logsanalysis.py

logsanalysis.py has 3 function that analysis the database for 3 topics.

Those 3 topics are :

#### 1.  What are the most popular three articles of all time?

> **def top3_articles(db)**<br>
> Function top3_articles takes a connection object as argument and will execute
> a query to get top 3 most viewed articles and print it.


#### 2. Who are the most popular article authors of all time?

> **def most_viewedAuthor(db)**<br>
> Function most_viewedAuthor takes a connection object as argument and will execute
> a query to get the list authors on the bases of total page views of their articles and print it in descending order.

#### 3. On which days did more than 1% of requests lead to errors?

> **def most_errorRequest(db)**<br>
> Function most_errorRequest takes a connection object as argument and will execute
> a query to analysis on what days did the users got more than 1% of 404 Not Found error and print the days.

### newsdata.sql

newsdata.sql is available at udacity's webiste.
[Click Here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to get it
and then run this command ```psql -d news -f newsdata.sql```.

## To Run

Open python in terminal
```
$ python3
Python 3.5.2 (default, Sep 14 2017, 22:51:06)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import logsanalysis
>>> logsanalysis.main()

```

or create a .py file and write
```
import logsanalysis
logsanalysis.main()
```
or just run the following commands
```
$ cd Logs-Analysis-Project
$ python3 logsanalysis.py
```
