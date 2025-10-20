i=3
while i>0:
	pasasword = input('pease enter your password:')
	if pasasword =='12345':
		print('sucess!')
		break
	else:
		i=i-1
		print('you have', i, 'more chance')

if i == 0:
	print('invalid login')