def encr(plaintext,key_1,key_2):
	import math
	alpha="abcdefghijklmnopqrstuvwxyz"
	input_string=plaintext
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
	input_string=output_string
	input_key=key_2
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
			cipher_text=alpha[(string_index+key_index)%26]
			cipher_blocks[string_blocks.index(i)].append(cipher_text)

	output_string_list=[]
	for i in cipher_blocks:
		output_string_list.extend(i)

	output_string=''.join(output_string_list)
	return output_string