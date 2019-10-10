while True:
	mode = input ('Please fill in game mode: ')
	if mode == 'q':
		break
	elif mode == '1':
		print ('Start mode one')
	elif mode == '2':
		print ('Start mode two')
	else:
		print ('Only can choose mode 1 or 2')