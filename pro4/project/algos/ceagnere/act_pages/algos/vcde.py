def decr(ciphertext,c_key_1,c_key_2):
	import math
	c_alpha='abcdefghijklmnopqrstuvwxyz'
	c_input_string=ciphertext
	c_input_key=c_key_2
	c_input_string_list=[i.lower() for i in c_input_string if i in c_alpha]
	c_input_key_list=[i.lower() for i in c_input_key if i in c_alpha]
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
			c_string_index=c_alpha.index(i[j])
			c_key_index=c_alpha.index(c_input_key[j])
			c_cipher_text=c_alpha[(c_string_index-c_key_index+26)%26]
			c_cipher_blocks[c_string_blocks.index(i)].append(c_cipher_text)

	c_output_string_list=[]
	for i in c_cipher_blocks:
		c_output_string_list.extend(i)

	c_output_string=''.join(c_output_string_list)
	c_alpha=c_alpha[::-1]
	c_input_string=c_output_string
	c_input_key=int(c_key_1)
	c_input_string_list=[i for i in c_input_string]
	c_output_string_list=[]
	for i in c_input_string_list:
		c_lower_i=i.lower()
		if i in c_alpha:
			c_indexpo=c_alpha.index(i)
			c_output_string_list.append(c_alpha[(c_indexpo+c_input_key)%26])
		elif c_lower_i in c_alpha:
			c_indexpo=c_alpha.index(c_lower_i)
			c_output_string_list.append(c_alpha[(c_indexpo+c_input_key)%26].upper())
		else:
			c_output_string_list.append(i)
	c_output_string=''.join(c_output_string_list)
	return c_output_string