number = int(input())

res = True
if (not number == 0) or (not number == 1):
	for i in range(2, number):
		if number%i == 0:
			res = False

if res:
	print('The number is Prime.')
elif (number == 0) or  (number == 1):
	print('The number is not Prime.')
else:
	print('The number is not Prime.')

