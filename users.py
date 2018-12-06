users = ['Tom','Tony','Admin','Amy','Eric']
for user in users:
	if user=='admin':
		print('hello ' +user+', you look handsome.')

	else:
		print('hello '+user+', thank you for logging in .')


if users = []:
	print("oh no")
else:
	print("nice")


current_users = ['Tom','Tony','Admin','Amy','Eric']
new_users = ['Liv','Livia','lisa','amy','tony']


for new_user in new_users:
	if new_user.upper() in current_users:
		print('Maybe change another name')
	elif new_user.lower() in current_users:
		print('Maybe change another name')
	elif new_user.title() in current_users:
		print('Maybe change another name')
	else:
		print('available')