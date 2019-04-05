#!C:\Users\sailakshmi01.trn.ITLINFOSYS\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type: text/html \n")
import cgi

form=cgi.FieldStorage()
import math
def printmatrix():
    global c_output_list
    c_output_list=[]
    for i in c_plain_list:
        c_output_list.extend(i)
        
def printcipher_list(row_size,col_size):
    m=0
    n=0
    delimit=0
    global c_output_list
    c_output_list=[]
    if col_size==1:
        c_output_list=c_cipher_list[0][::-1]
    else:
        while m<row_size and n<col_size:
            for i in range(col_size-1,m-1,-1):
                c_plain_list[i][row_size-1]=c_input_string_list[delimit]
                delimit+=1
            row_size-=1
            for i in range(row_size-1,n-1,-1):
                c_plain_list[m][i]=c_input_string_list[delimit]
                delimit+=1
            m+=1
            for i in range(m,col_size):
                c_plain_list[i][n]=c_input_string_list[delimit]
                delimit+=1
            n+=1
            for i in range(n,row_size):
                c_plain_list[col_size-1][i]=c_input_string_list[delimit]
                delimit+=1
            col_size-=1
        printmatrix()    
c_input_string=form.getvalue('name_pliantext')
c_input_key=int(form.getvalue('name_key2'))
c_input_string_list=[i for i in c_input_string]
c_len_string=len(c_input_string_list)
c_division=math.ceil(c_len_string/c_input_key)
c_cipher_list=[[] for i in range(c_division)]
delimiter=0
for i in range(c_division):
    for j in range(c_input_key):
        if delimiter<c_len_string:
            c_cipher_list[i].append(c_input_string_list[delimiter])
            delimiter+=1
        else:
            c_cipher_list[i].append('X')
c_plain_list=c_cipher_list.copy()
row_size=c_input_key
col_size=len(c_cipher_list)
printcipher_list(row_size,col_size)


while 'X' in c_output_list:
    c_output_list.remove('X')
c_output_string=''.join(c_output_list)

alpha="abcdefghijklmnopqrstuvwxyz"
alpha=alpha[::-1]
input_string=c_output_string
input_key=int(form.getvalue('name_key1'))
input_string_list=[i for i in input_string]
output_string_list=[]
for i in input_string_list:
    lower_i=i.lower()
    if i in alpha:
        indexpo=alpha.index(i)
        output_string_list.append(alpha[(indexpo+input_key)%26])
    elif lower_i in alpha:
        indexpo=alpha.index(lower_i)
        output_string_list.append(alpha[(indexpo+input_key)%26].upper())
    else:
        output_string_list.append(i)
output_string=''.join(output_string_list)
print(output_string)
