def encr(plain_text,key_1,key_2):
    alpha="abcdefghijklmnopqrstuvwxyz"
    alpha=alpha[::-1]
    input_string=plain_text
    input_key=int(key_1)
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




    c_input_string=output_string
    c_input_key=int(key_2)
    c_input_string_list=[i for i in c_input_string]
    c_len_string=len(c_input_string_list)
    c_cipher_block=['-' for i in range(c_len_string)]
    c_cipher_block_list=[c_cipher_block.copy() for i in range(c_input_key)]
    c_direct=0
    c_box=0

    for j in range(c_len_string):
        if c_box==0:
            c_direct=0
        elif c_box==c_input_key-1:
            c_direct=1
        c_cipher_block_list[c_box][j]="*"
        if c_direct==0:
            c_box+=1
        else:
            c_box-=1
    c_posi=0
    for i in range(c_input_key):
        for j in range(c_len_string):
            if c_cipher_block_list[i][j]=="*":
                c_cipher_block_list[i][j]=c_input_string[c_posi]
                c_posi+=1
    c_output_string_list=[]
    c_direct=0
    c_box=0
    for j in range(c_len_string):
        if c_box==0:
            c_direct=0
        elif c_box==c_input_key-1:
            c_direct=1
        c_output_string_list.append(c_cipher_block_list[c_box][j])
        if c_direct==0:
            c_box+=1
        else:
            c_box-=1
    c_output_string=''.join(c_output_string_list)
    return c_output_string

#i=input("Enter the text:")
#i1=int(input("key1:"))
#i2=int(input("key2:"))
#print(encr(i,i1,i2))
