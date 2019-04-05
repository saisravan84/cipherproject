def decr(plain_text,key_1,key_2):
    input_string=plain_text
    input_depth=int(key_2)
    input_string_list=[i for i in input_string]
    alpha="abcdefghijklmnopqrstuvwxyz"
    accepted_list=[]
    for i in input_string_list:
        if i.lower() in alpha:
            accepted_list.append(i)
    len_accepted_list=len(accepted_list)
    encrypted_list=[]
    for i in range(input_depth):
        encrypted_list.append([])
    direction=0
    j=0
    for i in accepted_list:
        if(direction==0):
            encrypted_list[j].append(i)
            j+=1
            if j==input_depth:
                direction=1
                j-=1
        else:
            j-=1
            encrypted_list[j].append(i)
            if j==0:
                direction=0
                j+=1
    output_list=[''.join(i) for i in encrypted_list]
    output_string="".join(output_list)
    c_input_string=output_string
    c_input_key=int(key_1)
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
    return c_output_string

#i=input("Enter the text:")
#i1=int(input("key1:"))
#i2=int(input("key2:"))
#print(decr(i,i1,i2))
