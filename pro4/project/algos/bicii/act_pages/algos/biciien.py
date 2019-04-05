def encr(plain_text,key_1):
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
        else:
            output_string_list.append(i)
    input_string =''.join(output_string_list);
    encrypted_array = [];
    for letter in input_string:
            bin_value = bin(ord(letter))[2:];
            if len(bin_value) < 8:
                    length = 8 - len(bin_value);
                    binary = '';
                    while length != 0:
                            binary = binary + '0';
                            length -= 1;
                    bin_value = binary + bin_value;
            encrypt_bin = bin_value[0:2] + bin_value[2:6][::-1] + bin_value[6:8];
            encrypted_array.append(chr(int(encrypt_bin,2)));
    encrypt = ''.join(encrypted_array);
    return encrypt
