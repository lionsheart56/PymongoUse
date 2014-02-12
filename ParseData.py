# use lxml to parse html string , removing something we dont want 
# a lot of function need to be implemented in the future

'''
	class type :

		self.parser
		self.data

	Usage: 

	  1. create an object 

	     object = ParseDate()

	     and then, you have a object.parser for etree.HTMLParser

	  2. import string data into this etree parser

	  	 object.initData( datainput )

	  3. use function to remove tag whatever you want 

	     object.removeTag( TagName )


'''

from lxml import etree
from StringIO import StringIO

class ParseData:
	def __init__(self):
		
		self.parser = etree.HTMLParser()

	def initData(self,inputData):
		
		self.data = etree.parse(StringIO(inputData),self.parser)

	def removeTag(self,tagName):
		tag = '//' + tagName

		for s in self.data.xpath(tag):
			s.getparent().remove(s)

	def turnString(self,tagName):

		tag = '//' + tagName

		for s in self.data.xpath(tag):
			makedData = etree.tostring(s)

		return makedData
	

