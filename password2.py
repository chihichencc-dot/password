i=3
while i>0:
	i=i-1
	pasasword = input('pease enter your password:')
	if pasasword =='12345':
		print('sucess!')
		break
	else:
		print('invalid login')
		if i>0:
			print('you have', i, 'more chance')