number = int(input())

res = True

for i in range(2, number):
	if number%i == 0:
		res = False

if res:
	print('The number is Prime.')
elif number == 0 or number == 1 or res:
	print('The number is not Prime.')

