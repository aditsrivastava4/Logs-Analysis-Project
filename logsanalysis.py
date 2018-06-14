#!/usr/bin/env python3

import calendar
import psycopg2 as psql

from datetime import datetime


# Top 3 most viewed articles
def top3_articles(db):
    get_data = db.cursor()
    get_data.execute(
        '''
            select count(path)as num, title from
            log,articles where path like '%' || slug || '%' and status='200 OK'
            group by title
            order by num desc limit 3;
        '''
    )
    data = get_data.fetchall()

    print('What are the most popular three articles of all time?')
    for x in data:
        print('\"{}\" - {} views'.format(x[1], x[0]))


# Most viewed authors
def most_viewedAuthor(db):
    get_data = db.cursor()
    get_data.execute(
        '''
            select name,count(name) as num from
            (select authors.id,articles.author,name,slug from authors
            join articles on authors.id = articles.author) as data,log
            where path like '%' || slug || '%' and status='200 OK'
            group by name order by num desc;
        '''
    )
    data = get_data.fetchall()

    print('Who are the most popular article authors of all time?')
    for x in data:
        print('{} - {} views'.format(x[0], x[1]))


# On which days did more than 1% of requests lead to errors?
def most_errorRequest(db):
    get_data = db.cursor()
    get_data.execute(
        '''
            select * from
            (select error.date,
            (round((100 * err::decimal/ok::decimal),2)) as percent from
            (select time::timestamp::date as date,
            count(time::timestamp::date) as err from log
            where status != '200 OK' group by time::timestamp::date
            order by time::timestamp::date nulls first) as error
            join
            (select time::timestamp::date as date,
            count(time::timestamp::date) as ok from log
            where status = '200 OK' group by time::timestamp::date
            order by time::timestamp::date nulls first) as okk
            on error.date=okk.date) as main where percent>1;
        '''
    )
    data = get_data.fetchall()

    print('On which days did more than 1% of requests lead to errors?')
    for x in data:
        print(
            '{} {}, {} - {}% errors'.format(
                calendar.month_name[x[0].month],
                x[0].day,
                x[0].year,
                x[1])
        )


def main():
    db = psql.connect(database='news')
    # connect() creates the database session
    # and returns new connection object

    # passing connection object db to all 3 functions
    top3_articles(db)
    print('\n')
    most_viewedAuthor(db)
    print('\n')
    most_errorRequest(db)
    db.close()
    # closing the database session


if __name__ == '__main__':
    main()
