# Use pymongo library for connect to mongodb
# a lot of function need to be coded in the future

'''
 Usage:

  instance = ConnectDB()

  instance.choosedb("lions")

  === giving database name ===

  instance.chooseCollection("one")

  === giving collection name of this database (like "table" in mysql) ===

  ins_id = instance.insertRec(record)

  === record was formated by JSON ===

  AllRec = instance.findAll()

  === return all record in this collection === 

 Variables:

 	ConnectDB.db is the database name

 	ConnectDB.table is the collection 
 	

'''

import pymongo
from pymongo import MongoClient

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

	def findGT(self,field,cmp,mode):
	#  find the record which "field" is greater than cmp value
	#  mode 1 for greater than ro equal to , others for only greater than

	    if mode == 1:
	        return self.table.find({field:{"$gte":cmp}})
	    else 
	        return self.table.find({field:{"$gt":cmp}})

	def findLT(self,field,cmp):
	#  find the record which "field" is less than cmp value
	#  mode 1 for less than or equal to , others for only less than

	    if mode == 1:
	        return self.table.find({field:{"$lte":cmp}})
	    else 
	        return self.table.find({field:{"$lt":cmp}})
	        