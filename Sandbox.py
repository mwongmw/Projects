#!/bin/python

import boto3
import time
import subprocess

ec = boto3.client('ec2', region_name= 'us-east-1')


g = '\033[92m'
s = '\033[0m'


def vertica():
  v = raw_input("Enter version (ie.5890): ")

  ec.create_tags(Resources=['i-0c3f0e10620a9ecb0'],Tags=[{'Key':'rptservice-version', 'Value':'1.0.{}'.format(v)}])
  print("{}version changed to {}{}".format(g,v,s))
  a = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.9.104', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
  print(a.stdout.read())
  time.sleep(5)
  v = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.9.104', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
  print(v.stdout.read())


def check():
  print("If new verion is not shown, re-run rc.local")

  print("1. Vertica")
  print("2. Exit")
  a = raw_input("Enter: ")

  if a == '1':
    r = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.9.104', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(r.stdout.read())
    v = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.9.104', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(v.stdout.read())
    check()
  elif a == '2':
    exit()
  else:
    check()

def version(v):
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'bidder-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'db-datamodel-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'db-geo-schema-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'db-schema-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'db-sitemgmt-schema-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'dcm-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'device-list-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'pws-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'rptcube-service-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-00179d125b16c1a0d'],Tags=[{'Key':'rptforecast-legacy-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'rptforecast-service-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'rptforecast-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'rptservice-legacy-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'rptservice-version', 'Value':"1.0.{}".format(v)}])
#  ec.create_tags(Resources=['i-00179d125b16c1a0d'],Tags=[{'Key':'ui-version', 'Value':"1.0.{}".format(v)}])
#  ec.create_tags(Resources=['i-00179d125b16c1a0d'],Tags=[{'Key':'ws-version', 'Value':"1.0.{}".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'ui-version', 'Value':"1.0.{}-tomcat9".format(v)}])
  ec.create_tags(Resources=['i-03a8ae60951e3954e','i-00179d125b16c1a0d'],Tags=[{'Key':'ws-version', 'Value':"1.0.{}-tomcat9".format(v)}])

  print("{}versions changed to {}{}".format(g,v,s))
  time.sleep(5)

#def dbrefresh():
 # a = raw_input("db-refresh? y/n: ")
  #if a == 'y':
   # ec.create_tags(Resources=['i-00179d125b16c1a0d'],Tags=[{'Key':'db-refresh', 'Value':'True'}])
   # print("{}db-refresh{}".format(g,s))
  #elif a == 'n':
   # ec.create_tags(Resources=['i-00179d125b16c1a0d'],Tags=[{'Key':'db-refresh', 'Value':'False'}])
  #else:
   # dbrefresh()

def restart():
  subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.10.10', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
#  subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.10.177', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
  subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.10.160', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
  time.sleep(10)

def verify():
#  wk = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.10.177', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
#  print("Walkme Version:")
#  print(wk.stdout.read())
#  time.sleep(5)
  sb = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.10.10', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
  print("Sandbox Version:")
  print(sb.stdout.read())
  time.sleep(5)
  uat = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.10.160', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
  print("UAT1 Version:")
  print(uat.stdout.read())

def rclocal():
  print("If new verion is not shown, re-run rc.local")
  print("1. Check Version")
  print("2. Walkme")
  print("3. Sandbox")
  print("4. UAT1")
  print("5. Exit")
  r = raw_input("Enter: ")

  if r == "1":
    verify()
    rclocal()
  if r == "2":
    subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.10.177', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
    rclocal()
  if r == "3":
    subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.10.10', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
    rclocal()
  if r == "4":
    subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.10.160', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
    rclocal()
  if r == "5":
    exit()
  else:
    rclocal()

def main():
  print("1.Vertica")
  print("2.Sandbox, UAT")
  print("3.Sandbox or UAT restart")
  a = raw_input("Enter: ")

  if a == '1':
    print("{}Vertica{}".format(g,s))
    vertica()
    check()
  elif a == '2':
    print("{}Sandbox, UAT{}".format(g,s))
    a = raw_input("Enter version (ie.5890): ")
    version(a)
   # dbrefresh()
    restart()
    verify()
    rclocal()
  elif a =='3':
    rclocal()
  else:
    main()

main()

