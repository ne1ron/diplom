#import htmlPy
#from main import app as htmlPy_app
import bd
import os

class AutoAnnotation():
	def doAnnotation(self,text):
		f= open("C:\Python34\diplom\input.txt","w")
		f.write(text)
		f.close()
		os.system('C:\Python34\diplom\do-it.bat')
		self.mergeResults()
	def mergeResults(self):
		os.system('C:\Python34\python.exe C:\Python34\diplom\merge.py -m C:\Python34\diplom\mout.txt -g C:\Python34\diplom\gout.gra -o C:\Python34\diplom\output.txt -i C:\Python34\diplom\lindex.txt')
		self.saveResult("C:\Python34\diplom\output.txt")
	def saveResult(self,way):
		print ("bb")
		
		

		
class SaveData():
	def addText(self,nameT):
		filop = "C:\Python34\diplom\lindex.txt"
		sqlC="CREATE TABLE `"+nameT+"` (`id` int(11) NOT NULL, `lexem` text NOT NULL, `start` int(11) NOT NULL,  `end` int(11) NOT NULL, `mystem` text NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
		sqlPK = "ALTER TABLE `"+nameT+"` ADD PRIMARY KEY (`id`);"
		sqlAI ="ALTER TABLE `"+nameT+"`	MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;"
		sqlI = "INSERT INTO `"+nameT+"` (`lexem`,`start`,`end`, `mystem`) VALUES %s"
		bd.c.SQL(sqlC)
		bd.c.SQL(sqlPK)
		bd.c.SQL(sqlAI)
		f = open(filop,"r")
		k = f.read()
		print (k)
		rez = k.split()
		print (rez)
		for i in rez:
			st = i[1:-1]
			ar = st.split("/")
			sql = "('%s', %s, %s, '%s')" % (ar[3],ar[1],ar[2],ar[4])
			per = sqlI % sql
			print (per)
			zap = per.encode('utf-8','ignore')
			zap = zap.decode("utf-8")
			bd.c.SQL(zap)
			
	def updateText(self):
		print ("uT")
	def getTextList(self):
		print ("gtl")
	def delText(self):
		print ("dT")

class SchemeManager():
	def addScheme(self,name,comm):
		print ("oppa"+name+" "+comm+" ")
		rez = bd.c.SQL("INSERT INTO scheme (`name`, `command`, `output`) VALUES ('"+name+"','"+comm+"','"+name+"');")
		print (rez)
	def delScheme(self):
		print ("uppa")
	def getList(self):
		rez = bd.c.SQL("SELECT * FROM scheme")
		for i in rez:
			print (i["name"])
		#print ("gL")
		
class SearchEngine():
	def doSQL(self,sql):
		return bd.c.SQL(sql)
	def workSearch(self):
		print ("wS")