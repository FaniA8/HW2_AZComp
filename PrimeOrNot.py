number = int(input())

res = False
if not number == 0:
	if not number == 1:
		res = True
		for i in range(2, number):
			if number%i == 0:
				res = False

if res:
	print('The number is Prime.')
else:
	print('The number is not Prime.')

