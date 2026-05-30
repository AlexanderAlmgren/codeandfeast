def binarytodecimal(binary: str) -> int:
	place = 128
	value = 0
	for i in binary:
		if(i == '1'):
			value += place
		place /= 2

	return int(value) 

def decimaltobinary(decimal: int) -> str:
	binary = list('00000000')
	place = 128
	for i in range(len(binary)):
		if(decimal >= place):
			decimal -= place
			binary[i] = '1'

		place /= 2

	return "".join(binary)

while True:
	try:
		line = input()

		if(len(line) == 8):
			print(binarytodecimal(line))

		else:
			print(decimaltobinary(int(line)))

	except EOFError:
		break

