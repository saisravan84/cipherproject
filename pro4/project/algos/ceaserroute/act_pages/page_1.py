#!C:\Users\sailakshmi01.trn.ITLINFOSYS\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type: text/html \n")
import cgi

form=cgi.FieldStorage()
import math
alpha="abcdefghijklmnopqrstuvwxyz"
c_input_string=form.getvalue('name_pliantext')
c_input_key=int(form.getvalue('name_key1'))
c_input_string_list=[i for i in c_input_string]
c_output_string_list=[]
for i in c_input_string_list:
    c_lower_i=i.lower()
    if i in alpha:
        c_indexpo=alpha.index(i)
        c_output_string_list.append(alpha[(c_indexpo+c_input_key)%26])
    elif c_lower_i in alpha:
        c_indexpo=alpha.index(c_lower_i)
        c_output_string_list.append(alpha[(c_indexpo+c_input_key)%26].upper())
    else:
        c_output_string_list.append(i)
c_output_string=''.join(c_output_string_list)


def printcipher_list(row_size,col_size):
    m=0
    n=0
    global output_list
    output_list=[]
    if col_size==1:
        output_list=cipher_list[0][::-1]
    else:
        while m<row_size and n<col_size:
            for i in range(col_size-1,m-1,-1):
                output_list.append(cipher_list[i][row_size-1])
            row_size-=1
            for i in range(row_size-1,n-1,-1):
                output_list.append(cipher_list[m][i])
            m+=1
            for i in range(m,col_size):
                output_list.append(cipher_list[i][n])
            n+=1
            for i in range(n,row_size):
                output_list.append(cipher_list[col_size-1][i])
            col_size-=1
        
    
input_string=c_output_string
input_key=int(form.getvalue('name_key2'))
alpha='abcdefghijklmnopqrstuvwxyz'
input_list=[i for i in input_string]
input_string_list=[]
for i in input_list:
    if i.lower() in alpha:
        input_string_list.append(i)
len_string=len(input_string_list)
division=math.ceil(len_string/input_key)
cipher_list=[[] for i in range(division)]
delimiter=0
for i in range(division):
    for j in range(input_key):
        if delimiter<len_string:
            cipher_list[i].append(input_string_list[delimiter])
            delimiter+=1
        else:
            cipher_list[i].append('X')

row_size=input_key
col_size=len(cipher_list)
printcipher_list(row_size,col_size)
output_string=''.join(output_list)
print(output_string)

