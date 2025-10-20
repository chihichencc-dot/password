i=0
while i<3:
	pasasword = input('pease enter your password:')
	if pasasword =='12345':
		print('sucess!')
		break
	else:
		i=i+1
		j=3-i
		print('you have', j, 'more chance')

if i == 3:
	print('invalid login')