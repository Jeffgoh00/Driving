country = input ('Where are you from: ')
age = int (input ('Please fill in your age: '))

if country == 'malaysia':
	if age >= 17:
		print ('You can driving')
	else:
		print ('You still cant driving')