password = input('Enter password: ')
my_password = len(password)
if my_password < 6:
	print ('Password is too short')
if my_password > 20:
	print ('Password is too long')
if (my_password >= 6)&(my_password <= 20):
	print ('*' * my_password)
