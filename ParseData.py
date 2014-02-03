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
	