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
		f= open("C:\Python34\diplom\input.txt","w")
		k = f.read()
		f.close()
		sqlAdT="INSERT INTO `texts` (`author`,`filename`,`tablename`,`text`) VALUES ('user','temp.txt','banzai1','%s');" %k;
		
	def updateText(self):
		print ("uT")
	def getTextList(self):
		rez = bd.c.SQL("SELECT * FROM `texts`")
		for i in rez:
			print (i["author"]+" "")
			print (i["text"])
	def delText(self,id):
		bd.c.SQL("DELETE FROM `texts` WHERE `id`="+str(id))

class SchemeManager():
	def addScheme(self,name,comm):
		print ("oppa"+name+" "+comm+" ")
		rez = bd.c.SQL("INSERT INTO scheme (`name`, `command`, `output`) VALUES ('"+name+"','"+comm+"','"+name+"');")
		print (rez)
	def delScheme(self,id):
		bd.c.SQL("DELETE FROM `scheme` WHERE `id`="+str(id))
	def getList(self):
		rez = bd.c.SQL("SELECT * FROM scheme")
		for i in rez:
			print (i["name"])
		
class SearchEngine():
	def doSQL(self,sql):
		return bd.c.SQL(sql)
	def workSearch(self, text):
		rez = self.doSQL("SELECT * FROM banzai1 WHERE `lexem`="+text+";")
		print (rez)