#!/bin/python

import sys
import argparse
import os
import re
import subprocess

parser = argparse.ArgumentParser ()
parser.add_argument("-a", "--add", nargs="+", dest="addservers", help="add server")
parser.add_argument("-r", "--remove", nargs="+", dest="removeservers", help="remove server")
parser.add_argument("-s", "--restart", nargs="+", dest="restartservers", help="restart server")
parser.add_argument("-stop", "--st", nargs="+", dest="stopservers", help="stop server")
parser.add_argument("-start", "--sst", nargs="+", dest="startservers", help="start server")
parser.add_argument("-reset", "--set", nargs="+", dest="resetservers", help="reset server")
parser.add_argument("-lg", "--logs", nargs="+", dest="checklogs", help="check logs")
args = parser.parse_args()


add = args.addservers
remove = args.removeservers
restart = args.restartservers
stop = args.stopservers
start = args.startservers
reset = args.resetservers
logs = args.checklogs



a = re.sub(r'.ads',r'-ads', str(add))
r = re.sub(r'.ads',r'-ads', str(remove))
s = re.sub(r'.ads',r'-ads', str(restart))
st1 = re.sub(r'.ads',r'-ads', str(stop))
sst = re.sub(r'.ads',r'-ads', str(start))
st = re.sub(r'.ads',r'-ads', str(reset))
lg1  = re.sub(r'-ads',r'.ads', str(logs))


ad = re.sub(r'[[\],\']', '', str(a))
rm = re.sub(r'[[\],\']', '', str(r))
s1 =  re.sub(r'[[\],\']', '', str(s))
st2 = re.sub(r'[[\],\']', '', str(st1))
sst2 = re.sub(r'[[\],\']', '', str(sst))
st3 = re.sub(r'[[\],\']', '', str(st))
lg2 =  re.sub(r'[[\]\']', '', str(lg1))


add_server = ad.split(" ")
remove_server = rm.split(" ")
restart_server = s1.split(" ")
stop_server = st2.split(" ")
start_server = sst2.split(" ")
reset_server = st3.split(" ")
check_logs = lg2.replace(" ", "")

null = open(os.devnull, 'w')

class lb():
  def start(self):
    try:
      subprocess.check_output(["gcloud compute instances start '%s' --project=unison-cloud --zone=us-east4-a" % a, ],shell=True, stderr=null)
    except Exception:
      try:
        subprocess.check_output(["gcloud compute instances start '%s' --project=unison-cloud --zone=us-east4-b" % a, ],shell=True, stderr=null)
      except Exception:
        try:
          subprocess.check_output(["gcloud compute instances start '%s' --project=unison-cloud --zone=us-east4-c" % a, ],shell=True, stderr=null)
        except Exception:
          try:
            subprocess.check_output(["gcloud compute instances start '%s' --project=unison-cloud --zone=us-west1-a" % a, ],shell=True, stderr=null)
          except Exception:
            try:
              subprocess.check_output(["gcloud compute instances start '%s' --project=unison-cloud --zone=us-west1-b" % a, ],shell=True, stderr=null)
            except Exception:
              try:
                subprocess.check_output(["gcloud compute instances start '%s' --project=unison-cloud --zone=us-west1-c" % a, ],shell=True, stderr=null)
              finally:
                pass
def stop(self):
      try:
           subprocess.check_output(["gcloud compute instances stop '%s' --project=unison-cloud --zone=us-east4-a" % a, ],shell=True, stderr=null)
      except Exception:
           try:
                subprocess.check_output(["gcloud compute instances stop '%s' --project=unison-cloud --zone=us-east4-b" % a, ],shell=True, stderr=null)
           except Exception:
                try:
                     subprocess.check_output(["gcloud compute instances stop '%s' --project=unison-cloud --zone=us-east4-c" % a, ],shell=True, stderr=null)
                except Exception:
                     try:
                          subprocess.check_output(["gcloud compute instances stop '%s' --project=unison-cloud --zone=us-west1-a" % a, ],shell=True, stderr=null)
                     except Exception:
                          try:
                               subprocess.check_output(["gcloud compute instances stop '%s' --project=unison-cloud --zone=us-west1-b" % a, ],shell=True, stderr=null)
                          except Exception:
                               try:
                                    subprocess.check_output(["gcloud compute instances stop '%s' --project=unison-cloud --zone=us-west1-c" % a, ],shell=True, stderr=null)
                               finally:
                                    pass
  def remove_lb(self):
      try:
            subprocess.check_output(["gcloud compute instance-groups unmanaged remove-instances ash1-serve-a --instances='%s' --project=unison-cloud --zone=us-east4-a" % r, ],shell=True, stderr=null)
            print("{} removed from the load balancer".format(r))
      except Exception:
           try:
                subprocess.check_output(["gcloud compute instance-groups unmanaged remove-instances ash1-serve-b --instances='%s' --project=unison-cloud --zone=us-east4-b" % r, ],shell=True, stderr=null)
                print("{} removed from the load balancer".format(r))
           except Exception:
                try:
                     subprocess.check_output(["gcloud compute instance-groups unmanaged remove-instances ash1-serve-c --instances='%s' --project=unison-cloud --zone=us-east4-c" % r, ],shell=True, stderr=null)
                     print("{} removed from the load balancer".format(r))
                except Exception:
                     try:
                          subprocess.check_output(["gcloud compute instance-groups unmanaged remove-instances pdx1-serve-a --instances='%s' --project=unison-cloud --zone=us-west1-a" % r, ],shell=True, stderr=null)
                          print("{} removed from the load balancer".format(r))
                     except Exception:
                          try:
                               subprocess.check_output(["gcloud compute instance-groups unmanaged remove-instances pdx1-serve-b --instances='%s' --project=unison-cloud --zone=us-west1-b" % r, ],shell=True, stderr=null)
                               print("{} removed from the load balancer".format(r))
                          except Exception:
                               try:
                                    subprocess.check_output(["gcloud compute instance-groups unmanaged remove-instances pdx1-serve-c --instances='%s' --project=unison-cloud --zone=us-west1-c" % r, ],shell=True, stderr=null)
                                    print("{} removed from the load balancer".format(r))
                               except Exception:
                                    try:
                                         print("{} not found in load balancer".format(r))
                                    finally:
                                         pass

  def add_lb(self):
      try:
           subprocess.check_output(["gcloud compute instance-groups unmanaged add-instances ash1-serve-a --instances='%s' --project=unison-cloud --zone=us-east4-a" % a, ],shell=True, stderr=null)
           print("{} added to the load balancer".format(a))
      except Exception:
           try:
                subprocess.check_output(["gcloud compute instance-groups unmanaged add-instances ash1-serve-b --instances='%s' --project=unison-cloud --zone=us-east4-b" % a, ],shell=True, stderr=null)
                print("{} added to the load balancer".format(a))
           except Exception:
                try:
                     subprocess.check_output(["gcloud compute instance-groups unmanaged add-instances ash1-serve-c --instances='%s' --project=unison-cloud --zone=us-east4-c" % a, ],shell=True, stderr=null)
                     print("{} added to the load balancer".format(a))
                except Exception:
                    try:
                         subprocess.check_output(["gcloud compute instance-groups unmanaged add-instances pdx1-serve-a --instances='%s' --project=unison-cloud --zone=us-west1-a" % a, ],shell=True, stderr=null)
                         print("{} added to the load balancer".format(a))
                    except Exception:
                         try:
                              subprocess.check_output(["gcloud compute instance-groups unmanaged add-instances pdx1-serve-b --instances='%s' --project=unison-cloud --zone=us-west1-b" % a, ],shell=True, stderr=null)
                              print("{} added to the load balancer".format(a))
                         except Exception:
                              try:
                                   subprocess.check_output(["gcloud compute instance-groups unmanaged add-instances pdx1-serve-c --instances='%s' --project=unison-cloud --zone=us-west1-c" % a, ],shell=True, stderr=null)
                                   print("{} added to the load balancer".format(a))
                              except Exception:
                                   try:
                                        print("Please check {}".format(a))
                                   finally:
                                        pass

v = lb()

class pepper:

    def __init__(self, host, command='sudo ls /data/logs/stream/ | wc -l'):
      self.host = host
      self.command = command
      os.system("pepper -T -L '{}' cmd.run '{}'".format(host, command))





if add is None and remove is None and stop is None and start is None and reset is None and logs is None:
        for r in restart_server:
          v.remove_lb()

        s = re.sub(r'-ads',r'.ads', str(restart))
        s1 =  re.sub(r'[[\]\']', '', str(s))
        rs = s1.replace(" ", "")

        os.system("pepper -T -L '%s' cmd.run 'salt-call state.apply glassfish.upgrade'" % rs)
        s = re.sub(r'.ads',r'-ads', str(restart))
        s1 =  re.sub(r'[[\],\']', '', str(s))
        restart_server = s1.split(" ")


        for a in restart_server:
          v.add_lb()

elif add is None and remove is None and restart is None and start is None and reset is None and logs is None:
     for a in stop_server:
          v.stop()
          print("{} updated".format(a))

elif add is None and remove is None and restart is None and stop is None and reset is None and logs is None:

     for a in start_server:
          v.start()
          print("{} updated".format(a))

elif add is None and restart is None and stop is None and start is None and reset is None and logs is None:
     for r in remove_server:
          v.remove_lb()

elif add is None and remove is None and restart is None and stop is None and start is None and logs is None:
     for a in reset_server:
          v.stop()

     for a in reset_server:
          v.start()
          print("{} reset".format(a))

elif add is None and remove is None and restart is None and stop is None and start is None and reset is None:

     pepper(check_logs)

else:

     for a in add_server:
          v.add_lb()


