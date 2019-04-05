def encr(plaintext,key_1,key_2):
	import math
	input_string=plaintext
	input_depth=int(key_1)
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
	c_input_key=key_2
	c_input_string_list=[i.lower() for i in c_input_string if i in alpha]
	c_input_key_list=[i.lower() for i in c_input_key if i in alpha]
	c_input_string_len=len(c_input_string_list)
	c_input_key_len=len(c_input_key_list)
	c_division=math.ceil(c_input_string_len/c_input_key_len)
	c_string_blocks=[[] for i in range(c_division)]
	c_cipher_blocks=[[] for i in range(c_division)]
	c_delimiter=0
	i=0
	for i in range(len(c_string_blocks)):
		for j in range(c_input_key_len):
			if c_delimiter<c_input_string_len:
				c_string_blocks[i].append(c_input_string_list[c_delimiter])
				c_delimiter+=1

	for i in c_string_blocks:
		for j in range(len(i)):
			c_string_index=alpha.index(i[j])
			c_key_index=alpha.index(c_input_key[j])
			c_cipher_text=alpha[(c_string_index+c_key_index)%26]
			c_cipher_blocks[c_string_blocks.index(i)].append(c_cipher_text)

	c_output_string_list=[]
	for i in c_cipher_blocks:
		c_output_string_list.extend(i)

	c_output_string=''.join(c_output_string_list)
	return c_output_string


#text=input("enter the input text:")
#key_1=int(input("enter the key1(integer): "))
#key_2=input("enter the key2(string): ")
#print("the encrypted text is :",encr(text,key_1,key_2))
