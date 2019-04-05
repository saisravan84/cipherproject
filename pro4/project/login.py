#!C:\Users\sailakshmi01.trn.ITLINFOSYS\AppData\Local\Programs\Python\Python37\python.exe
print("Content-Type: text/html \n")
import pymysql
import cgi
import cgitb
connection = pymysql.connect(host="localhost", user="root", passwd="", database="UI")
cursor = connection.cursor()
cgitb.enable()
f=cgi.FieldStorage()
username=f.getvalue("username");
password=f.getvalue("pass");
pass1=""
select_query="select UserName,Password from UserDetails where UserName='%s'"
cursor.execute(select_query % username)
records=cursor.fetchall()
if password:
	for row in records:
		user=row[0]
		pass1=row[1]
	if password==pass1:
		redirectURL = "index.html"
		print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
	else:
		print('''<html><head><script type="text/javascript">alert("Passwords doesnt match");</script></head></html>''')
connection.close()
print('''
<html>
<head>
<title>
Login
</title>
<link href="https://fonts.googleapis.com/css?family=Ubuntu+Condensed" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
<style>
*{
font-family: 'Ubuntu Condensed', sans-serif;
font-size:18px;
}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  #background-color:red;
  
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #fff;
  text-decoration:none;
  color:#333;
}

body
{
background-image:url("bg2.jpg");
#background-color:#333;
background-repeat:no-repeat;
background-size:100% 100%;
overflow:hidden;
opacity:1;
}
.f1 {
width:380px;
height:250px;
margin-top:100px;
margin-bottom:150px;
background-color:#fdf4f4;
padding-top:40px;
padding-bottom:40px;
border-radius:20px;
}


.button{
color: #fff;
background-color:#333;
width: 100px;
height:40px;
border-radius:5px;
font-weight:bold;
}
.button:hover{
color: #333;
background-color: #fff;
}

.qw1{
	float:right;
	position: relative;
	right: 200px;
	top:30px;
}

</style>
</head>
<body>
<div class="f3">
<div class="f2">
<ul>
  <li><a href="#about">Home</a></li>
  <li style="float:right"><a  href="sign.py">SignUp</a></li>
  <li style="float:right"><a  href="login.py">LogIn</a></li>
</ul>
</div>
<div class="qw1">
<form name="login" action="" method="POST">


<div class="f1">
<center>
<p><b><i>Login Here!!!</i></b></p>
<div class="container">
<div class="form-group">
<div class="input-group">
<div class="input-group-addon">
<span class="glyphicon glyphicon-user"></span> 
</div>
<input class="form-control" id="email" name="username" type="text" placeholder="Username" style="width:300px;"/>
</div>
</div>
<div class="form-group">
<div class="input-group">
<div class="input-group-addon">
<span class="glyphicon glyphicon-lock"></span> 
</div>
<input class="form-control" id="email" name="pass" type="password" placeholder="Password" style="width:300px;"/>
</div>
</div>
</div>
<div class="form-group">
<input type="submit" align="center" value="Login" class="button">
</div>
</center>
</div>
</form>
</div>
</div>
</body>
</html>''')
