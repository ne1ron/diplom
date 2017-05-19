import os
import htmlPy
from back_end import BackEnd, getMenu
from work import *
import json


man = SchemeManager()
ann = AutoAnnotation()
sd = SaveData()
se = SearchEngine()


class dForm(htmlPy.Object):
    def __init__(self, app):
        super(dForm, self).__init__()
        self.app = app
    @htmlPy.Slot(str)
    def form_function_name(self, json_data):
        form_data = json.loads(json_data)
        man.addScheme(form_data["sname"],form_data["coms"])
    @htmlPy.Slot(str)
    def addtext(self, jsd):
        form_data = json.loads(jsd)
        ann.doAnnotation(form_data["text"])
        print (form_data["text"])
        sd.addText("banzai1")
    @htmlPy.Slot(str)
    def search(self, jsd):
        form_data = json.loads(jsd)
        se.workSearch(form_data["slovo"])
        print (form_data["slovo"])


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# GUI initializations
app = htmlPy.AppGUI(title=u"Application", maximized=True, plugins=True)


# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")
app.bind(BackEnd(app))
app.bind(dForm(app))

app.template = ("index.html", {"navmenu":getMenu(0)})

if __name__ == "__main__":
    app.start()