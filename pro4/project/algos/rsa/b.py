#!C:\Users\sailakshmi01.trn.ITLINFOSYS\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type: text/html \n")
import cgi

form=cgi.FieldStorage()
plain_text=form.getvalue('name_pliantext')
key_1=int(form.getvalue('name_key1'))




p=13
#int(input('Enter a prime no p: '))
q=7
#int(input('Enter a prime no q: '))
#print("prime numbers are:\np=" + str(p) + ", q=" + str(q) + "\n")
n=p*q
#print("n = p * q = " + str(n) + "\n")
phi=(p-1)*(q-1)
#print("[phi(n)]: " + str(phi) + "\n")

def decrypt_char(m,d,n):
    c = m**d % n
    return c
def decrypt_string(s,a,b):
    d=a
    n=b
    q=s
    numbers="1234567890"
    
    len_string=len(q)
    i=0
    a_list=[]
    while i<len_string:
        if q[i] in numbers and i+1<len_string:
            a_list.append(q[i]+q[i+1])
            i+=2
        else:
            a_list.append(q[i])
            i+=1
        
    list1=a_list
    list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v'
           ,'w','x','y','z','?',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
           ,'Q','R','S','T','U','V','W','X','Y','Z','@','#','!','.','$','%','&','*','(',')','-','+']

    out=[]
    count=1
    for i in list1:
        if i in list2:
            for j in list2:
                if i==j:
                    out.append(count)
                    count=1
                    break
                else:
                    count=count+1
        else:
            out.append(int(i))
        
    final=[]
    for i in out:
        p=decrypt_char(i,d,n)
        final.append(p)
    
    final1=[]

    for i in final:
        final1.append(list2[i-1])
    final2= ''.join(final1)
    return final2

def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l

#print("Choose an e from a below coprimes array:\n")
#print(str(coprimes(phi)) + "\n")
e=int(key_1)
d= modinv(e,phi)
#print("decrypted keys are (d=" + str(d) + ", n=" + str(n) + ").\n")

s =plain_text
#print("\nPlain message: " + s + "\n")
dec = str(decrypt_string(s,d,n))
#print("decrypted message: " + dec + "\n")
print(dec)


