import htmlPy

def getMenu(par):
	shab = '''
<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-2">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="https://iloveliveuzia.wordpress.com">SfA&S</a>
    </div>

    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-2">
      <ul class="nav navbar-nav">
        %s
      </ul>
      <ul class="nav navbar-nav navbar-right">
        %s
      </ul>
    </div>
  </div>
</nav>
	'''
	res = ""
	mas = [\
	'<li %s ><a href="BackEnd.gmain" data-bind="true">Главная %s</a></li>',\
	'<li %s ><a href="BackEnd.addtext" data-bind="true">Добавить текст %s</a></li>',\
	'<li %s ><a href="BackEnd.addscheme" data-bind="true">Добавить свою разметку %s</a></li>',\
    '<li %s><a href="BackEnd.search" data-bind="true">Поиск %s</a></li>',\
    '<li %s ><a href="BackEnd.corpus" data-bind="true">Коллекция %s</a></li>']
	for i in range(0,len(mas)):
		if (i==par):
			res +=mas[i] %('class="active"','<span class="sr-only">(current)</span>')+"\n"
		else:
			res += mas[i] % ("","")+"\n"
	second = '<li %s><a href="BackEnd.about" data-bind="true">О программе %s</a></li>'
	if par==5:
		second = second % ('class="active"','<span class="sr-only">(current)</span>') 
	else:
		second = second %("","")
	priz = shab % (res,second)
	return priz

class BackEnd(htmlPy.Object):
	def __init__(self, app):
		super(BackEnd, self).__init__()
		self.app = app

	@htmlPy.Slot()
	def addtext(self):
		self.app.template = ("./addtext.html", {"navmenu":getMenu(1)})
		
	@htmlPy.Slot()
	def gmain(self):
		self.app.template = ("./index.html", {"navmenu":getMenu(0)})
		
	@htmlPy.Slot()
	def search(self):
		self.app.template = ("./search.html",{"navmenu":getMenu(3)})
		
	@htmlPy.Slot()
	def corpus(self):
		self.app.template = ("./corpus.html", {\
		"rows":[{"name":"текст1","part":"Часть текста первого в выдаче"},{"name":"текст2","part":"Часть текста второго в выдаче"}],\
		"navmenu":getMenu(4)
		})
		
	@htmlPy.Slot()
	def about(self):
		self.app.template = ("./about.html", {"navmenu":getMenu(5)})
		
	@htmlPy.Slot()
	def addscheme(self):
		self.app.template = ("./addscheme.html",{"navmenu":getMenu(2)})