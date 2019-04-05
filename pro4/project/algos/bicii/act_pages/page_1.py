#!C:\Users\sailakshmi01.trn.ITLINFOSYS\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type: text/html \n")
import cgi
from algos import biciien as al
form=cgi.FieldStorage()
plain_text=form.getvalue('name_pliantext')
key_1=int(form.getvalue('name_key1'))
a=al.encr(plain_text,key_1)
print(a)
