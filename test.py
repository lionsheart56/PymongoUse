import pycurl
import time
import pymongo
from pymongo import MongoClient
from lxml import etree
from StringIO import StringIO
from time import gmtime, strftime
#-*- coding: utf8 -*-

class GetPage:
    def __init__ (self, url):
        self.contents = ''
        self.url = url

    def read_page (self, buf):
        self.contents = self.contents + buf

    def show_page (self):
        print self.contents
    def return_data (self):
    	return self.contents


class ConnectDB:

	def choosedb(self,dbname):
		client = MongoClient()
		self.db = client[dbname]
	
	# connecting to mongodb and choose a database, if not exits, create one by itself
	
	def chooseCollection(self,coname):
		self.table=self.db[coname]

	def insertRec(self,record):	
		
		post_id=self.table.insert(record)
		return post_id
	# insert record to database and return it's id
	
	def findAll(self):
		return self.table.find()




instance = ConnectDB()
instance.choosedb("lions")
instance.chooseCollection("one")

# client = MongoClient()
# db = client.test_database
# posts=db.posts

for x in range(10):
    mypage = GetPage("http://udn.com/NEWS/BREAKINGNEWS/")
    testcurl = pycurl.Curl()
    testcurl.setopt(testcurl.URL, mypage.url)
    testcurl.setopt(testcurl.WRITEFUNCTION, mypage.read_page)
    testcurl.perform()
    testcurl.close()  
    # use curl to fetch website source code


    source_data=mypage.return_data()
    source_data = source_data.decode('utf-8', 'ignore')

    parser = etree.HTMLParser()

    tree = etree.parse(StringIO(source_data), parser)

    for s in tree.xpath('//script'):
        s.getparent().remove(s)
    for s in tree.xpath('//noscript'):
        s.getparent().remove(s)
    for s in tree.xpath('//style'):
	    s.getparent().remove(s)
    for s in tree.xpath('//body'):
	    NoScriptData = etree.tostring(s)

    # use lxml parser to delete script and parse only body content

    Size = len(NoScriptData)
    Time = strftime("%Y-%m-%d %H:%M:%S")

    print Size,
    print "  at  ",
    print Time

    post = {"Size":Size,
    		"Time":Time}
    
    # post_id=posts.insert(post)    
    # insert record to database
    # print post_id
    ins_id = instance.insertRec(post)

AllRec = instance.findAll()

for a in AllRec:
	print a
	# for all record in the db, print them
   
 








