def decr(ciphertext,c_key_1,c_key_2):
	import math
	alpha='abcdefghijklmnopqrstuvwxyz'
	input_string=ciphertext
	input_key=c_key_2
	input_string_list=[i.lower() for i in input_string if i in alpha]
	input_key_list=[i.lower() for i in input_key if i in alpha]
	input_string_len=len(input_string_list)
	input_key_len=len(input_key_list)
	division=math.ceil(input_string_len/input_key_len)
	string_blocks=[[] for i in range(division)]
	cipher_blocks=[[] for i in range(division)]
	delimiter=0
	i=0
	for i in range(len(string_blocks)):
		for j in range(input_key_len):
			if delimiter<input_string_len:
				string_blocks[i].append(input_string_list[delimiter])
				delimiter+=1

	for i in string_blocks:
		for j in range(len(i)):
			string_index=alpha.index(i[j])
			key_index=alpha.index(input_key[j])
			cipher_text=alpha[(string_index-key_index+26)%26]
			cipher_blocks[string_blocks.index(i)].append(cipher_text)

	output_string_list=[]
	for i in cipher_blocks:
		output_string_list.extend(i)

	output_string=''.join(output_string_list)
	c_input_string=output_string
	c_input_key=int(c_key_1)
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

#text=input("enter the encrypted text:")
#key_1=int(input("enter the key1(integer): "))
#key_2=input("enter the key2(string): ")
#print("the plain text is :",decr(text,key_1,key_2))
