#!/bin/python

import boto3
import time
import subprocess
import os

ec = boto3.client('ec2', region_name= 'us-east-1')
ecw = boto3.client('ec2', region_name= 'us-west-2')
null = open(os.devnull, 'w')

g = '\033[92m'
s = '\033[0m'

print("1. East and West")
print("2. East 10.55.8.81 and 10.55.18.30")
print("3. West 10.30.4.97")
print("4. East 10.55.8.81")
print("5. East 10.55.18.30")
server = raw_input("Enter: ")


def version():
  if server == '1':
    print("{}East and West Bidder soaks{}").format(g,s)
    v = raw_input("Enter version (ie.5890): ")
    ec.create_tags(Resources=['i-0b3bc020208f8436e'],Tags=[{'Key':'bidder-version', 'Value':"1.0.{}-jdk15".format(v)}])
    ec.create_tags(Resources=['i-085e7e40004c8d55d'],Tags=[{'Key':'bidder-version', 'Value':"1.0.{}-jdk15".format(v)}])
    ecw.create_tags(Resources=['i-00924d7dcc53d53fc'],Tags=[{'Key':'bidder-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}Version changed to {}{}".format(g,v,s))

  elif server == '2':
    print("{}East Bidder 10.55.8.97 and 10.55.8.81{}").format(g,s)
    v = raw_input("Enter version (ie.5890): ")
    ec.create_tags(Resources=['i-0b3bc020208f8436e'],Tags=[{'Key':'bidder-version', 'Value':"1.0.{}-jdk15".format(v)}])
    ec.create_tags(Resources=['i-085e7e40004c8d55d'],Tags=[{'Key':'bidder-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}East Version changed to {}{}".format(g,v,s))

  elif server == '3':
    print("{}West Bidder 10.30.4.97{}").format(g,s)
    v = raw_input("Enter version (ie.5890): ")
    ecw.create_tags(Resources=['i-00924d7dcc53d53fc'],Tags=[{'Key':'bidder-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}West version changed to {}{}".format(g,v,s))

  elif server == '4':
    print("{}East Bidder 10.55.8.81{}").format(g,s)
    v = raw_input("Enter version (ie.5890): ")
    ec.create_tags(Resources=['i-0b3bc020208f8436e'],Tags=[{'Key':'bidder-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}East 10.55.11.113 version changed to {}{}".format(g,v,s))

elif server == '5':
    print("{}East Bidder 10.55.18.30{}").format(g,s)
    v = raw_input("Enter version (ie.5890): ")
    ec.create_tags(Resources=['i-085e7e40004c8d55d'],Tags=[{'Key':'bidder-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}East 10.55.2.14 version changed to {}{}".format(g,v,s))
  else:
    exit()

def remove_lb():
  if server == "1":
    bid1 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-bidders-int-us-east-1 --instances i-0b3bc020208f8436e", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid1.stdout.read())
    print("Removed 10.55.8.81 from the load balancer")
    bid2 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-bidders-int-us-east-3 --instances i-085e7e40004c8d55d", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid2.stdout.read())
    print("Removed 10.55.18.30 from the load balancer")
    bid3 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-bidders-testing-int-us-west-2 --instances i-00924d7dcc53d53fc --region us-west-2" , ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid3.stdout.read())
    print("Removed 10.30.4.97 from the load balancer")
  if server == "2":
    bid1 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-bidders-int-us-east-1 --instances i-0b3bc020208f8436e", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid1.stdout.read())
    print("Removed 10.55.8.81 from the load balancer")
    bid2 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-bidders-int-us-east-3 --instances i-085e7e40004c8d55d", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid2.stdout.read())
    print("Removed 10.55.18.30 from the load balancer")
  if server == "3":
    bid3 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-bidders-testing-int-us-west-2 --instances i-00924d7dcc53d53fc --region us-west-2" , ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid3.stdout.read())
    print("Removed 10.30.4.97 from the load balancer")
  if server == "4":
    bid1 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-bidders-int-us-east-1 --instances i-0b3bc020208f8436e", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid1.stdout.read())
    print("Removed 10.55.8.81 from the load balancer")
  if server == "5":
    bid2 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name ci-bidders-int-us-east-3 --instances i-085e7e40004c8d55d", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid2.stdout.read())
    print("Removed 10.55.18.30 from the load balancer")
  else:
    pass

def restart():

  if server == "1":
    bid1 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.8.81', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid1.stdout.read())
    print("i-0ea01a305cabc43bd restarted")
    bid2  = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.18.30', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid2.stdout.read())
    print("i-038757c7c18bc7cba restarted")
    bid3 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.30.4.97', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid3.stdout.read())
    print("i-005c5157d977f34f9 restarted")
  elif server == "2":
    bid1 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.8.81', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid1.stdout.read())
    print("i-0ea01a305cabc43bd restarted")
    bid2  = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.18.30', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid2.stdout.read())
    print("i-038757c7c18bc7cba restarted")
  elif server == "3":
    bid3 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.30.4.97', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid3.stdout.read())
    print("i-005c5157d977f34f9 restarted")
  elif server == "4":
    bid1 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.8.81', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid1.stdout.read())
    print("i-0ea01a305cabc43bd restarted")
  elif server == "5":
    bid2  = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.18.30', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid2.stdout.read())
    print("i-038757c7c18bc7cba restarted")
  else:
    pass


def verify():
  if server == "1":
    bid1 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.8.81', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.8.81:")
    print(bid1.stdout.read())
    time.sleep(5)
    bid2 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.18.30', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.18.30:")
    print(bid2.stdout.read())
    time.sleep(5)
    bid3 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.30.4.97', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.30.4.97:")
    print(bid3.stdout.read())

  elif server == "2":
    bid1 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.8.81', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.8.81:")
    print(bid1.stdout.read())
    time.sleep(5)
    bid2 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.18.30', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.18.30:")
    print(bid2.stdout.read())

  elif server == "3":
    bid3 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.30.4.97', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.30.4.97:")
    print(bid3.stdout.read())
  elif server == "4":
    bid1 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.8.81', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.8.81:")
    print(bid1.stdout.read())
    time.sleep(5)
  elif server == "5":
    bid2 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.18.30', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.18.30:")
    print(bid2.stdout.read())
  else:
    pass

def add_lb():
  print("")
  print("Enter host when ready to return to the load balancer or restart the server:")
  print("")
  print("http://10.55.8.81:8080/d/utils/dserverHealthStatus.jsp")
  print("http://10.55.18.30:8080/d/utils/dserverHealthStatus.jsp")
  print("http://10.30.4.97:8080/d/utils/dserverHealthStatus.jsp")
  print("")
  print("{}Add to load balancer{}:").format(g,s)
  print("1. i-0b3bc020208f8436e/10.55.8.81")
  print("2. i-085e7e40004c8d55d/10.55.18.30")
  print("3. i-00924d7dcc53d53fc/10.30.4.97")
  print("4. Check version")
  print("{}Restart Server:{}").format(g,s)
  print("5. Restart i-0b3bc020208f8436e/10.55.8.81")
  print("6. Restart i-085e7e40004c8d55d/10.55.18.30")
  print("7. Restart i-00924d7dcc53d53fc/10.30.4.97")
  print("8. exit")
  print("")
  a = raw_input("Enter:")
   if a == '1':
    bid1 = subprocess.Popen(["aws elb register-instances-with-load-balancer --load-balancer-name ci-bidders-int-us-east-1 --instances i-0b3bc020208f8436e", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid1.stdout.read())
    print("Added 10.55.8.81 to load balancer")
    add_lb()
  elif a == '2':
    bid2 = subprocess.Popen(["aws elb register-instances-with-load-balancer --load-balancer-name ci-bidders-int-us-east-3 --instances i-085e7e40004c8d55d", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid2.stdout.read())
    print("Added 10.55.18.30 to load balancer")
    add_lb()
  elif a == '3':
    bid3 = subprocess.Popen(["aws elb register-instances-with-load-balancer --load-balancer-name ci-bidders-testing-int-us-west-2 --instances i-00924d7dcc53d53fc --region us-west-2", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid3.stdout.read())
    print("Added 10.30.4.97 to load balancer")
    add_lb()
  elif a == '4':
    verify()
    add_lb()
  elif a == '5':
    bid1 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.8.81', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid1.stdout.read())
    print("i-0ea01a305cabc43bd restarted")
    bid1 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.8.81', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.18.81:")
    print(bid1.stdout.read())
    add_lb()
  elif a == '6':
    bid2  = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.18.30', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid2.stdout.read())
    print("i-038757c7c18bc7cba restarted")
    bid2 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.18.30', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.18.30:")
    print(bid2.stdout.read())
    add_lb()
  elif a == '7':
    bid3 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.30.4.97', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(bid3.stdout.read())
    print("i-005c5157d977f34f9 restarted")
    bid3 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.30.4.97', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.30.4.97:")
    print(bid3.stdout.read())
    add_lb()
  elif a == '8':
    exit()
  else:
    add_lb()

version()
remove_lb()
restart()
verify()
add_lb()


