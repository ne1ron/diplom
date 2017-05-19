import pymysql.cursors

class BD():
	def __init__(self):
		self.connection = pymysql.connect(host='localhost', port=3306, user='mysql', password='mysql' , db="sfas", cursorclass=pymysql.cursors.DictCursor,charset='utf8')
		self.cur = self.connection.cursor()
	def SQL(self,x):
		print (x)
		self.cur.execute(x,())
		self.connection.commit()
		return self.cur
c = BD()