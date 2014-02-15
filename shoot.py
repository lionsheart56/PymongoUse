# save fetch record to database
# format:
#     url    -    time     -   size    -   diff 

import pycurl
import pymongo
import time
from ParseData import ParseData
from GetPage import GetPage
from ConnectDB import ConnectDB
from time import gmtime, strftime


instance = ConnectDB()
instance.choosedb("Fetch")
instance.chooseCollection("YouTube")


url = "http://www.youtube.com"

mypage = GetPage(url)
curlconnect = pycurl.Curl()
curlconnect.setopt(curlconnect.URL, mypage.url)
curlconnect.setopt(curlconnect.WRITEFUNCTION, mypage.read_page)
curlconnect.perform()
curlconnect.close()

source_data = mypage.return_data()
source_data = source_data.decode('utf-8', 'ignore')

parsing = ParseData()
parsing.initData(source_data)

parsing.removeTag("script")
parsing.removeTag("noscript")
plainData = parsing.turnString("body")

size = len(plainData)
time = strftime("%Y-%m-%d %H:%M:%S")



last = instance.table.find().sort("Time",-1)

if last.count() == 0:
	post = {"Url":url,"Size":size,
    		"Time":time,"Diff":0}
else:
	for a in last:
		oldSize = a["Size"]
		break
	diff = size - oldSize
	post = {"Url":url,"Size":size,
			"Time":time,"Diff":diff}

#ins_id = instance.insertRec(post)

AllRec = instance.findAll()

for a in AllRec:
	print a


print '\n'


test = instance.table.find({"Diff":{"$in":[18]}})

#print test
for a in test:
    ids = a["_id"]
instance.delByID(ids)
#test = instance.findGT("Diff",40)

#test=instance.table.find({"Diff":{"$gte":40}})
#for a in test:
#	print a

#print '\n'

AllRec = instance.findAll()

for a in AllRec:
	print a




