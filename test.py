filop = "C:\Python34\diplom\lindex.txt"
f = open(filop,"r")
k = f.read()
print (k)
rez = k.split()
print (rez)
for i in rez:
	st = i[1:-1]
	ar = st.split("/")
	sql = "(%s, %s, %s, %s, '%s')" % (ar[0],ar[3],ar[1],ar[2],ar[4])
	print (sql+"\n")
f.close()