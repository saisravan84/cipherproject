import math
def decr(plain_text,key_1,key_2):
    input_string=plain_text
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
    division=math.ceil(len_input_string/len_input_key)
    input_key_list_sort=input_key_list.copy()
    input_key_list_sort.sort()
    for i in range(len_input_key):
        letter_list=input_string_list[i*division:((i+1)*division)]
        cipher_dict[input_key_list_sort[i]].extend(letter_list)
    output_string_list=[]
    #print(cipher_dict)
    for i in range(division):
        for j in input_key_list:
            #print(f'{i}-{j}-{cipher_dict[j][i]}')
            output_string_list.append(cipher_dict[j][i])
    while '`' in output_string_list:
        output_string_list.remove('`')
    alpha="abcdefghijklmnopqrstuvwxyz"
    alpha=alpha[::-1]
    input_string=''.join(output_string_list)
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
    return output_string
