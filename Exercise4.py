country = input ('Where are you from: ')
age = int (input ('Please fill in your age: '))

if country == 'malaysia':
	if age >= 17:
		print ('You can driving')
	else:
		print ('You still cant driving')
elif country == 'us':
	if age >= 16:
		print ('You can driving')
	else:
		print ('You still cant driving')
else:
	print ('You only can type malaysia/us')