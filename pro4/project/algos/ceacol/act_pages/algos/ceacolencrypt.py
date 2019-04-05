import math
def encr(plain_text,key_1,key_2):
    alpha="abcdefghijklmnopqrstuvwxyz"
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
    input_string=''.join(output_string_list)
    #print(input_string)
    input_key=key_2
    input_string_list=[i for i in input_string]
    input_key_list=[]
    for i in input_key:
        if i not in input_key_list:
            input_key_list.append(i)
    input_key=''.join(input_key_list)
    cipher_dict={i:[] for i in input_key_list}
    len_input_string=len(input_string_list)
    len_input_key=len(input_key_list)
    for i in range(len_input_string):
        cipher_dict[input_key_list[i%len_input_key]].append(input_string_list[i])
    division=math.ceil(len_input_string/len_input_key)
    for i in cipher_dict:
        if len(cipher_dict[i])!=division:
            cipher_dict[i].append('`')
    #print(cipher_dict)
    input_key_list.sort()
    output_string=""
    for i in input_key_list:
        output_string+=''.join(cipher_dict[i])
    return output_string

