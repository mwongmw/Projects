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
print("2. East 10.55.11.113 and 10.55.2.14")
print("3. West 10.30.4.139")
print("4. East 10.55.11.113")
print("5. East 10.55.2.14")
server = raw_input("Enter: ")

def version():
#  v = raw_input("Enter version (ie.5890): ")
  if server == '1':
#East DCM
    print("East and West")
    v = raw_input("Enter version (ie.5890): ")
    ec.create_tags(Resources=['i-038757c7c18bc7cba'],Tags=[{'Key':'dcm-version', 'Value':"1.0.{}-jdk15".format(v)}])
    ec.create_tags(Resources=['i-0ea01a305cabc43bd'],Tags=[{'Key':'dcm-version', 'Value':"1.0.{}-jdk15".format(v)}])
#West DCM
    ecw.create_tags(Resources=['i-005c5157d977f34f9'],Tags=[{'Key':'dcm-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}Version changed to {}{}".format(g,v,s))

  elif server == '2':
    print("East 10.55.11.113 and 10.55.2.14")
    v = raw_input("Enter version (ie.5890): ")
    ec.create_tags(Resources=['i-038757c7c18bc7cba'],Tags=[{'Key':'dcm-version', 'Value':"1.0.{}-jdk15".format(v)}])
    ec.create_tags(Resources=['i-0ea01a305cabc43bd'],Tags=[{'Key':'dcm-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}East Version changed to {}{}".format(g,v,s))

  elif server == '3':
    print("West 10.30.4.139")
    v = raw_input("Enter version (ie.5890): ")
    ecw.create_tags(Resources=['i-005c5157d977f34f9'],Tags=[{'Key':'dcm-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}West version changed to {}{}".format(g,v,s))

  elif server == '4':
    print("East 10.55.11.113")
    v = raw_input("Enter version (ie.5890): ")
    ec.create_tags(Resources=['i-0ea01a305cabc43bd'],Tags=[{'Key':'dcm-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}East 10.55.11.113 version changed to {}{}".format(g,v,s))

  elif server == '5':
    print("East 10.55.2.14")
    v = raw_input("Enter version (ie.5890): ")
    ec.create_tags(Resources=['i-038757c7c18bc7cba'],Tags=[{'Key':'dcm-version', 'Value':"1.0.{}-jdk15".format(v)}])
    print("{}East 10.55.2.14 version changed to {}{}".format(g,v,s))
  else:
    exit()

def remove_lb():
  if server == "1":
#East DCM
    dcm1 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name dcm-int-soak --instances i-0ea01a305cabc43bd", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm1.stdout.read())
    print("Removed i-0ea01a305cabc43bd from dcm-int-soak")

    dcm2 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name dcm-int-soak-a --instances i-038757c7c18bc7cba", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm2.stdout.read())
    print("Removed i-038757c7c18bc7cba from dcm-int-soak-a")
#West DCM
    dcm3 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name dcm-int-soak --instances i-005c5157d977f34f9 --region us-west-2" , ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm3.stdout.read())
    print("Removed i-005c5157d977f34f9 from dcm-int-soak")
  if server == "2":
    dcm1 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name dcm-int-soak --instances i-0ea01a305cabc43bd", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm1.stdout.read())
    print("Removed i-0ea01a305cabc43bd from dcm-int-soak")

    dcm2 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name dcm-int-soak-a --instances i-038757c7c18bc7cba", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm2.stdout.read())
    print("Removed i-038757c7c18bc7cba from dcm-int-soak-a")
  if server == "3":
    dcm3 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name dcm-int-soak --instances i-005c5157d977f34f9 --region us-west-2" , ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm3.stdout.read())
    print("Removed i-005c5157d977f34f9 from dcm-int-soak")
  if server == "4":
    dcm1 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name dcm-int-soak --instances i-0ea01a305cabc43bd", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm1.stdout.read())
    print("Removed i-0ea01a305cabc43bd from dcm-int-soak")
  if server == "5":
    dcm2 = subprocess.Popen(["aws elb deregister-instances-from-load-balancer --load-balancer-name dcm-int-soak-a --instances i-038757c7c18bc7cba", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm2.stdout.read())
    print("Removed i-038757c7c18bc7cba from dcm-int-soak-a")
  else:
    pass


def restart():

  if server == "1":
    dcm1 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.11.113', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm1.stdout.read())
    print("i-0ea01a305cabc43bd restarted")
    dcm2  = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.2.14', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm2.stdout.read())
    print("i-038757c7c18bc7cba restarted")
    dcm3 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.30.4.139', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm3.stdout.read())
    print("i-005c5157d977f34f9 restarted")
  elif server == "2":
    dcm1 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.11.113', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm1.stdout.read())
    print("i-0ea01a305cabc43bd restarted")
    dcm2  = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.2.14', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm2.stdout.read())
    print("i-038757c7c18bc7cba restarted")
  elif server == "3":
    dcm3 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.30.4.139', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm3.stdout.read())
    print("i-005c5157d977f34f9 restarted")
  elif server == "4":
    dcm1 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.11.113', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm1.stdout.read())
    print("i-0ea01a305cabc43bd restarted")
  elif server == "5":
    dcm2  = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.2.14', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm2.stdout.read())
    print("i-038757c7c18bc7cba restarted")
  else:
    pass


def verify():
  if server == "1":
#East DCM
    dcm1 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.11.113', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.11.113:")
    print(dcm1.stdout.read())
    time.sleep(5)
    dcm2 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.2.14', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.2.14:")
    print(dcm2.stdout.read())
    time.sleep(5)
#West DCM
    dcm3 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.30.4.139', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.30.4.139:")
    print(dcm3.stdout.read())

  elif server == "2":
    dcm1 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.11.113', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.11.113:")
    print(dcm1.stdout.read())
    time.sleep(5)
    dcm2 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.2.14', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.2.14:")
    print(dcm2.stdout.read())

  elif server == "3":
    dcm3 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.30.4.139', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.30.4.139:")
    print(dcm3.stdout.read())
  elif server == "4":
    dcm1 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.11.113', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.11.113:")
    print(dcm1.stdout.read())
    time.sleep(5)
  elif server == "5":
    dcm2 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.2.14', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.2.14:")
    print(dcm2.stdout.read())
  else:
    pass

def add_lb():
  print("")
  print("Enter host when ready to return to the load balancer or restart the server:")
  print("")
  print("http://10.55.11.113:8080/dcm/utils/overallCacheStatus.jsp")
  print("http://10.55.2.14:8080/dcm/utils/overallCacheStatus.jsp")
  print("http://10.30.4.139:8080/dcm/utils/overallCacheStatus.jsp")
  print("")
  print("1. i-0ea01a305cabc43bd/10.55.11.113")
  print("2. i-038757c7c18bc7cba/10.55.2.14")
  print("3. i-005c5157d977f34f9/10.30.4.139")
  print("4. Check version")
  print("5. Restart i-0ea01a305cabc43bd/10.55.11.113")
  print("6. Restart i-038757c7c18bc7cba/10.55.2.14")
  print("7. Restart i-005c5157d977f34f9/10.30.4.139")
  print("8. exit")
  print("")
  a = raw_input("Enter:")

  if a == '1':
    dcm1 = subprocess.Popen(["aws elb register-instances-with-load-balancer --load-balancer-name  dcm-int-soak --instances i-0ea01a305cabc43bd", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm1.stdout.read())
    print("Added i-0ea01a305cabc43bd to dcm-int-soak")
    add_lb()
  elif a == '2':
    dcm2 = subprocess.Popen(["aws elb register-instances-with-load-balancer --load-balancer-name dcm-int-soak-a --instances i-038757c7c18bc7cba", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm2.stdout.read())
    print("Added i-038757c7c18bc7cba to dcm-int-soak-a")
    add_lb()

  elif a == '3':
    dcm3 = subprocess.Popen(["aws elb register-instances-with-load-balancer --load-balancer-name dcm-int-soak --instances i-005c5157d977f34f9 --region us-west-2", ],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm3.stdout.read())
    print("Added i-005c5157d977f34f9 to dcm-int-soak")
    add_lb()
  elif a == '4':
    verify()
    add_lb()
  elif a == '5':
    dcm1 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.11.113', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm1.stdout.read())
    print("i-0ea01a305cabc43bd restarted")
    dcm1 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.11.113', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.11.113:")
    print(dcm1.stdout.read())
    add_lb()
  elif a == '6':
    dcm2  = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.55.2.14', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm2.stdout.read())
    print("i-038757c7c18bc7cba restarted")
    dcm2 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.55.2.14', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.55.2.14:")
    print(dcm2.stdout.read())
    add_lb()
  elif a == '7':
    dcm3 = subprocess.Popen(["ssh {ut}@{server} {rc}".format(ut='ubuntu', server='10.30.4.139', rc='sudo /etc/rc.local')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(dcm3.stdout.read())
    print("i-005c5157d977f34f9 restarted")
    dcm3 = subprocess.Popen(["ssh {ut}@{server} {dcr}".format(ut='ubuntu', server='10.30.4.139', dcr='sudo docker ps')], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print("10.30.4.139:")
    print(dcm3.stdout.read())
    add_lb()
  elif a == '8':
    exit()
  else:
    add_lb()

version()
remove_lb()
restart()
add_lb()
