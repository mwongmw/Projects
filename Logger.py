#!/bin/python

import boto3
import time
import subprocess
import os
import requests

ec = boto3.client('ec2', region_name= 'us-east-1')
ecw = boto3.client('ec2', region_name= 'us-west-2')
null = open(os.devnull, 'w')

g = '\033[92m'
s = '\033[0m'


def check_schema():
  print("1. Deploy Logger")
  print("2. Check Schema")
  v = raw_input("Enter: ")

  if v == '1':
    pass
  elif v == '2':
    s = raw_input("Enter version (ie.1.0.12248-jdk15, enter 12248): ")
    s1 = subprocess.Popen(["/usr/local/bin/schema-diff {}".format(s)], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(s1.stdout.read())
    check_schema()
  else:
    check_schema()

check_schema()

print("1. East Logger")
print("2. West Logger")

r = raw_input("Enter: ")

instance = raw_input("Enter logger instance (ie.i-0b866d2c62e9c1e28): ")
server = raw_input("Enter server ip (ie.10.55.23.29): ")

def version(a):
#  v = raw_input("Enter version (ie.1.0.115566-jdk15, enter 115566): ")

  if r == '1':
#East Logger
    v = raw_input("Enter version (ie.1.0.12248-jdk15, enter 12248): ")
    ec.create_tags(Resources=['{}'.format(a)],Tags=[{'Key':'logger-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}Logger Version changed to {}{}".format(g,v,s))
  elif r == '2':
#West Logger
    v = raw_input("Enter version (ie.1.0.12248-jdk15, enter 12248): ")
    ecw.create_tags(Resources=['{}'.format(a)],Tags=[{'Key':'logger-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}Version changed to {}{}".format(g,v,s))
  else:
    exit()

def remove_lb(a):

  if r == "1":
#East Logger
    m1 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-ad-vpc-east --instances {} --region us-east-1".format(instance), ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(m1.stdout.read())
    print("Removed {} from the load balancer".format(a))

  elif r == "2":
#West Logger
    m3 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-ads-west-2-130814-1 --instances {} --region us-west-2".format(instance), ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(m3.stdout.read())
    print("Removed {} from the load balancer".format(a))
  else:
    remove_lb()

def restart(a):
  m1 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server=a, rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
  print(m1.stdout.read())
  print("{} restarted".format(a))

def status(a):
  m1 = subprocess.Popen(["ssh {ut}@{s} {dcr}".format(ut='ubuntu', s=a, dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
  print("{}:".format(a))
  print(m1.stdout.read())
  time.sleep(5)
  print("Check JSP:")
  print("http://{}:8080/d/utils/dserverHealthStatus.jsp".format(a))
  print("")

def add_lb(*args,**kwargs):
  print("")
  print("Add back to the load balancer or restart if new version is not shown:")
  print("")
  print("1. Add to load balancer")
  print("2. Restart {}".format(server))
  print("3. Verify")
  print("4. Exit")
  print("")
  e = raw_input("Enter:")

  if e == '1':
#East
    if r == '1':
      m2 = subprocess.Popen(["aws elb register-instances-with-load-balancer --load-balancer-name ci-ad-vpc-east --instances {} --region us-east-1".format(instance), ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
      print(m2.stdout.read())
      print("Added {} to the load balancer".format(instance))
      add_lb()
    elif r == '2':
#West
      m3 = subprocess.Popen(["aws elb register-instances-with-load-balancer --load-balancer-name ci-ads-west-2-130814-1 --instances {} --region us-west-2".format(instance), ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
      print(m3.stdout.read())
      print("Added {} to the load balancer".format(server))
      add_lb()
  elif e == "2":
    m1 = subprocess.Popen(["ssh {ut}@{s} {rc}".format(ut='ubuntu', s=server, rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(m1.stdout.read())
    time.sleep(5)
    print("{} restarted".format(server))
    add_lb()
  elif e == "3":
   m1 = subprocess.Popen(["ssh {ut}@{s} {dcr}".format(ut='ubuntu', s=server, dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
   print("{}:".format(server))
   print(m1.stdout.read())
   add_lb()
  elif e =="4":
    exit()
  else:
    add_lb()

version(instance)
remove_lb(instance)
restart(server)
status(server)
add_lb(instance,server)
