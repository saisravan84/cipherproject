#!C:\Users\sailakshmi01.trn.ITLINFOSYS\AppData\Local\Programs\Python\Python37\python.exe
print("Content-Type: text/html \n")
import cgi
import cgitb
cgitb.enable()
import pymysql
import cgi
import cgitb
connection = pymysql.connect(host="localhost", user="root", passwd="", database="UI")
cursor = connection.cursor()
#table_query = """CREATE TABLE UserDetails(UserName VARCHAR(20), Password VARCHAR(20), Gender VARCHAR(10), Email VARCHAR(20),
#MobileNo VARCHAR(10), City VARCHAR(20))"""
#cursor.execute(table_query)
cgitb.enable()
f=cgi.FieldStorage()
username=f.getvalue("username");
password=f.getvalue("pass");
confirmpassword=f.getvalue("pass1");
gender=f.getvalue("optradio");
email=f.getvalue("email");
number=f.getvalue("number");
city=f.getvalue("city");
if password:
	if password==confirmpassword:
		insert_query="""INSERT INTO UserDetails VALUES(%s,%s,%s,%s,%s,%s)"""
		insert_values=(username,password,gender,email,number,city)
		cursor.execute(insert_query,insert_values)
		redirectURL = "login.py"
		print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')
	else:
		print("Error")
connection.commit();
print('''<html>
<head>
<title>
Signup
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
  background-color: #111;
  text-decoration:none;
  color:white;
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
width: 400px;
height:450px;
padding: 20px;
margin-top:50px;
border: 1px solid;
border-radius:50px;
background-color:#fdf4f4;
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
<form name="f5" action="" method="POST">
<center>
<div class="f1">
<h5><b><i>Register Here!!!</i></b></h5>
<div class="form-group">
<div class="input-group">
<div class="input-group-addon">
<span class="glyphicon glyphicon-user"></span> 
</div>
<input class="form-control" id="email" name="username" type="text" placeholder="Username" pattern="^[a-zA-Z]+$" title="Username should contain Alphabets" required style="width:300px;"/>
</div>
</div>
<div class="form-group">
<div class="input-group">
<div class="input-group-addon">
<span class="glyphicon glyphicon-lock"></span> 
</div>
<input class="form-control"  name="pass" type="password" placeholder="Enter your Password"   required style="width:300px;"/>
</div>
</div>

<div class="form-group">
<div class="input-group">
<div class="input-group-addon">
<span class="glyphicon glyphicon-lock"></span> 
</div>
<input class="form-control"  name="pass1" type="password" placeholder="Confirm Password"  required style="width:300px;"/>
</div>
</div>

<div class="form-group">
<div class="input-group">

<label class="radio-inline control-label"><b>Gender</b></label>
<label class="radio-inline">
      <input type="radio" name="optradio" value="M">Male
    </label>
    <label class="radio-inline">
      <input type="radio" name="optradio" value="F">Female
    </label>
    <label class="radio-inline">
      <input type="radio" name="optradio" value="O">Others
    </label>
</div>
</div>


<div class="form-group">
<div class="input-group">
<div class="input-group-addon">
<span class="glyphicon glyphicon-envelope"></span> 
</div>
<input class="form-control"  name="email" type="email" placeholder="Enter your Email address" required style="width:300px;"/>
</div>
</div>

<div class="form-group">
<div class="input-group">
<div class="input-group-addon">
<span class="glyphicon glyphicon-earphone"></span> 
</div>
<input class="form-control"  name="number" type="text" placeholder="Enter your Mobile Number" pattern='^[0-9]{10}$' title="length should be 10" maxlength="10" minlength="10" required style="width:300px;"/>
</div>
</div>

<div class="form-group">
<div class="input-group">
<div class="input-group-addon">
<span class="glyphicon glyphicon-home"></span> 
</div>
<input class="form-control"  name="city" type="text" placeholder="Enter your City"  required style="width:300px;"/>
</div>
</div>
<div class="form-group">
<input type="submit" align="center" value="Login" class="button">
</div>
</div>
</center>
</form>
</div>
</div>
</body>
</html>
''')

