#!/bin/python

import subprocess
import smtplib
from email.MIMEText import MIMEText


sv = ['ash2-db012.sm-us','ash2-db030.sm-us','ord1-db010.sm-us','ord1-db011.sm-us','ord1-db012.sm-us','ord1-db021.sm-us','ord1-db030.sm-us','ord1-db031.sm-us','ord1-db032.sm-us','ord1-db100.sm-us']


def send():
   msg = MIMEText('test')
   msg["Subject"] = "Test"
   msg['From'] = "mwong@viantinc.com"
   msg['To'] = "mwong@viantinc.com"
   s = smtplib.SMTP("smtp.msprod.msp", 25)
   s.ehlo()
   s.sendmail("mwong@viantinc.com","mwong@viantinc.com",msg.as_string())
   s.quit()

for t in sv:
  a = subprocess.Popen(["ssh {server} '/usr/lib64/nagios/plugins/check_nrpe -H {rc} -c check_disk'".format(ut='ubuntu', server='ash2-nagp001.ops', rc=t)], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()

  #print(a[0][5:7])

  if (a[0][5:7]) == 'OK':
    print('ok')
  else:
    print('check',t)
    send()
