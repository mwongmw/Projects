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

print("East Soak A: i-0f92984cfc78eee0d / 10.55.2.244")
print("East Soak B: i-0be450a7d57ec357a / 10.55.10.99")
print("West Soak: i-0664966c78faf875e / 10.30.4.48")
print("")
print("East config: adelphic-prod-ash3-mediator-soak-a / adelphic-prod-ash3-mediator-soak-b")
print("West config: adelphic-prod-pdx2-mediator-soak-b")
print("")
print("1.East Mediator")
print("2.West Mediator")

r = raw_input("Enter: ")


instance = raw_input("Enter Soak Instance: ")
server = raw_input("Enter server ip: ")

def version(a):
  v = raw_input("Enter version (ie.5890): ")

  if r == '1':
#East Mediator
    ec.create_tags(Resources=['{}'.format(a)],Tags=[{'Key':'mediator-version', 'Value':"{}-arm".format(v)}])
    print("{}Version changed to {}{}".format(g,v,s))
  elif r == '2':
#West Mediator
    ecw.create_tags(Resources=['{}'.format(a)],Tags=[{'Key':'mediator-version', 'Value':"{}-arm".format(v)}])
    print("{}Version changed to {}{}".format(g,v,s))
  else:
    exit()

def remove_lb():

  if r == "1":
    print("1. Remove 10.55.2.244/i-0f92984cfc78eee0d from the load balancer")
    print("2. Remove 10.55.10.99/i-0be450a7d57ec357a from the load balancer")
    a = raw_input("Enter: ")
    if a == '1':
#East DCM
      m1 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-mediator-us-east-3 --instances i-0f92984cfc78eee0d", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
      print(m1.stdout.read())
      print("Removed 10.55.2.244 from the load balancer")
    elif a == '2':
      m1 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-mediator-us-east-1 --instances i-0be450a7d57ec357a", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
      print(m1.stdout.read())
      print("Removed 10.55.10.99 from the load balancer")
    else:
      remove_lb()

  elif r == "2":
#West DCM
    m3 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name pdx2-b-mediator --instances i-0664966c78faf875e --region us-west-2" , ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(m3.stdout.read())
    print("Removed 10.30.4.48 from the load balancer ")


def restart(a):
  m1 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server=a, rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
  print(m1.stdout.read())
  print("{} restarted".format(a))


def verify(a):
  m1 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server=a, dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
  print("{}:".format(a))
  print(m1.stdout.read())
  time.sleep(5)

def status(a):
  try:
    r = requests.get("http://{}:8080/status/".format(a))
    s = r.text
    if s == "up":
      print("http://{}:8080/status/ is: up".format(a))
    else:
      print("Check status: http://{}:8080/status/ ".format(a))
  except requests.exceptions.ConnectionError:
    print("http://{}:8080/status/ is: down".format(a))

def add_lb(a):
  print("1. Add to load balancer")
  print("2. Restart")
  print("3. Verify")
  print("4. Exit")
  print("")
  e = raw_input("Enter:")

  if e == '1':
    print("1. Add 10.55.2.244 to the load balancer")
    print("2. Add 10.55.10.99 to the load balancer")
    print("3. Add 10.30.4.48 to the load balancer")
    add = raw_input("Enter ")

    if add == '1':
#East
      m2 = subprocess.Popen(["aws elb register-instances-with-load-balancer --load-balancer-name ci-mediator-us-east-3 --instances i-0f92984cfc78eee0d", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
      print(m2.stdout.read())
      add_lb(a)
      print("Added 10.55.2.244 to the load balancer")
      add_lb(a)
    elif add == '2':
      m2 = subprocess.Popen(["aws elb register-instances-with-load-balancer --load-balancer-name ci-mediator-us-east-1 --instances i-0be450a7d57ec357a", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
      print(m2.stdout.read())
      print("Added 10.55.10.99 to the load balancer")
      print("Check status: http://{}:8080/status/ ".format(a))
      add_lb(a)

    elif add == '3':
#West
      m3 = subprocess.Popen(["aws elb register-instances-with-load-balancer --load-balancer-name pdx2-b-mediator --instances i-0664966c78faf875e --region us-west-2", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
      print(m3.stdout.read())
      print("Added 10.30.4.48 to the load balancer")
      add_lb(a)
    else:
      add_lb(a)
  elif e == "2":
    m1 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server=a, rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(m1.stdout.read())
    print("{} restarted".format(a))
    add_lb(a)
  elif e == "3":
   m1 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server=a, dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
   print("{}:".format(a))
   print(m1.stdout.read())
   add_lb(a)
  elif e =="4":
    exit()
  else:
   add_lb()

version(instance)
remove_lb()
restart(server)
verify()
status()
add_lb()
