import argparse
parser = argparse.ArgumentParser()

def gettext(strok):
	i=0
	s=""
	#print (strok)
	while i<len(strok):
		if (strok[i]=="{"):
			break
		s=s+strok[i]
		i=i+1
	return s
def getatr(strok):
	i=0
	s=""
	while i<len(strok):
		if (strok[i]=="{"):
			i+=1
			break
		i=i+1
	
	while i<len(strok):
		if (strok[i]=='}'):
			break
		s=s+strok[i]
		i+=1
	return s
	
def getgatr(st):
	j=0
	i=0
	s="a"
	while j<3:
		if (s == ' ')and(st[i]!=' '):
			j+=1
		s = st[i]
		i+=1
	res = st[i:]
	return res
parser.add_argument('-m', '--mystem' , help='mystem output in text format')
parser.add_argument('-g', '--graphan' , help='graphan output in gra')
parser.add_argument('-o', '--output' , help='output of script')
parser.add_argument('-i', '--index' , help='index to help find ')
parser.parse_args()

m = parser.parse_args().mystem
g = parser.parse_args().graphan
out = parser.parse_args().output
iout = parser.parse_args().index
fg = open(g, 'r', encoding="cp1251")
fm = open(m, 'r', encoding="cp1251")

infoout=open(iout,'w')
fout = open(out, 'w')

j = 0
a=[]
for i in fg:
	if str(i[0]).isalnum():
		#print (i)
		a.append(i)
		
b=[]
for i in fm:
	if str(i[0]).isalnum():
		#print (i)
		b.append(i)

start = 0
while j < len(b):
	text=gettext(b[j])
	minfo=getatr(b[j])
	#ginfo=getgatr(a[j])
	s = "<span id=\""+str(j+1)+"\" class='word' minfo=\""+minfo+"\" >"+text+"</span>\n"
	e = start + len(text)
	l = "["+str(j+1)+"/"+str(start)+"/"+str(e)+"/"+text+"/"+minfo+"]\n"
	start = e
	fout.write(s)
	infoout.write(l)
	j+=1

