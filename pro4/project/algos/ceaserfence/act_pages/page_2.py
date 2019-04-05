#!C:\Users\sailakshmi01.trn.ITLINFOSYS\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type: text/html \n")
import cgi
from algos import rfced as al
form=cgi.FieldStorage()
plain_text=form.getvalue('name_pliantext')
key_1=int(form.getvalue('name_key1'))
key_2=int(form.getvalue('name_key2'))
a=al.decr(plain_text,key_1,key_2)
print(a)
