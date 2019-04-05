def encr(plain_text,key_1,key_2):
    alpha="abcdefghijklmnopqrstuvwxyz 1234567890"
    input_string=plain_text
    input_key=int(key_1)
    input_string_list=[i for i in input_string]
    output_string_list=[]
    for i in input_string_list:
        lower_i=i.lower()
        if i in alpha:
            indexpo=alpha.index(i)
            output_string_list.append(alpha[(indexpo+input_key)%37])
        elif lower_i in alpha:
            indexpo=alpha.index(lower_i)
            output_string_list.append(alpha[(indexpo+input_key)%37].upper())
        else:
            output_string_list.append(i)
    output_string=''.join(output_string_list)
    input_string=output_string
    input_key=int(key_2)
    if input_key==0:
        input_key=5
    input_list=[i for i in input_string]
    input_string_list=[]
    alpha="abcdefghijklmnopqrstuvwxyz 1234567890"
    for i in input_list:
        if i in alpha:
            input_string_list.append(i)
    len_string=len(input_string_list)
    cipher_block=['-' for i in range(len_string)]
    cipher_block_list=[cipher_block.copy() for i in range(input_key)]
    direct=0
    box=0

    for j in range(len_string):
        if box==0:
            direct=0
        elif box==input_key-1:
            direct=1
        cipher_block_list[box][j]="*"
        if direct==0:
            box+=1
        else:
            box-=1
    for i in range(input_key):
        for j in range(len_string):
            if cipher_block_list[i][j]=="*":
                cipher_block_list[i][j]=input_string_list[j]
    output_string_list=[]
    for i in range(input_key):
        for j in range(len_string):
            if cipher_block_list[i][j]!="*":
                output_string_list.append(cipher_block_list[i][j])
    while '-' in output_string_list:
        output_string_list.remove("-")
    output_string=''.join(output_string_list)
    return output_string

#i=input("Enter the text:")
#i1=int(input("key1:"))
#i2=int(input("key2:"))
#print(encr(i,i1,i2))
        
            
        
