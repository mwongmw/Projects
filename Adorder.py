#!/bin/python

import os
import sys
import smtplib
import pymysql
from datetime import datetime, timedelta
from decimal import Decimal
import dateutil.parser

mysql_conn = pymysql.connect(host="10.55.1.32",
                                user="ci_ads",
                                passwd="H)gu$3NW",
                                db="ci_ads")
cur = mysql_conn.cursor()

print("1.Spend Percent Change")
print("2.Yesterdays Hour Spend")

select = raw_input("Enter: ")

now = datetime.now()
n = now.hour

c = "\033[92m"
c1 = "\033[96m"
c2 = "\033[0m"

def total_spend(self, *args, **kwargs):


  cur.execute("select ad_order_id, round(sum(total_spend),2), last_updated from CI_AD_ORDER_SPEND_LOG where log_date >= '{}' and log_date < '{}'and ad_order_id = '{}' order by last_updated asc;".format(date, to, order))
  data = cur.fetchall()
  dt = [tuple(map(str, i)) for i in data]
  for a in dt:
    print(a[2][-19:-8])

  for row in data:
    print row[1]
    return row[1]

def next_day_total(self, *args, **kwargs):
   date1 = datetime.strptime(date, "%Y-%m-%d")
   date2 = date1 +timedelta(days=1)

   to1 = datetime.strptime(to, "%Y-%m-%d")
   to2 = to1 +timedelta(days=1)

   cur.execute("select ad_order_id, round(sum(total_spend),2), last_updated from CI_AD_ORDER_SPEND_LOG where log_date >= '{}' and log_date < '{}'and ad_order_id = '{}' order by last_updated asc;".format(date2, to2, order))
   data5 =  cur.fetchall()
   print("\033[92mTotal Spend:\033[0m")
   day = [tuple(map(str, i)) for i in data5]
   for a in day:
    print(a[2][-19:-8])

   for row in data5:
    print row[1]
    return row[1]


def time():
  n1 = n/24.00
  n2 = Decimal(n1)
  return n2

def total_change(total_spend, next_day_total, time):
  if total_spend is None or next_day_total is None:
    pass
  else:
    c1 = float(total_spend)
    c2 = float(next_day_total)
    n3 = float(round(time,2))
    nt = int(n3*100)
    print("\33[92m{}% of Yesterday:\033[0m".format(nt))
    def percent(*args, **kwargs):
      pc = c1*n3
      print(pc)
      c3 = (c2-pc)/(pc)*100
      print("\033[92m% Change:\033[0m")
      return abs(round(c3,1))
    return percent

def hour_spend(self, *args, **kwargs):
  cur.execute("select log_date, ad_order_id, round(sum(total_spend),2), last_updated from CI_AD_ORDER_SPEND_LOG where last_updated >= '{}' and last_updated < '{}' and ad_order_id = '{}';".format(date, to, order))
  data2 = cur.fetchall()
  for row in data2:
    print row[0]
    print row[2]
    return row[2]

if select == "1":
  date = raw_input("Enter {}yesterdays{} UTC date(yyyy-mm-dd): ".format(c1,c2))
  to = raw_input("Enter {}todays{} UTC date(yyyy-mm-dd): ".format(c,c2))
  order = raw_input("Order ID: ")
  print("\033[92mTotal Spend:\033[0m")
  tc = total_change(total_spend('date', 'to', 'order'), next_day_total('date2', 'to2', 'order'), time())
  try:
    print(tc())
  except Exception:
    pass

elif select == "2":
  date = raw_input("Enter {}yesterdays{} UTC date and {}hour{}(yyyy-mm-dd hh): ".format(c1,c2,c1,c2))
  to = raw_input("Enter {}yesterdays{} UTC date and {}next{}{} hour{}(yyyy-mm-dd hh): ".format(c1,c2,c,c2,c1,c2))
  order = raw_input("Order ID: ")
  print("\033[92mHour Spend:\033[0m")
  hour_spend('date', 'to', 'order')
else:
  pass
