import random
import string

uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
all_numbers = list(string.digits)
password_symbols = list(['!', '%', '#', '&', '$', '@'])

choices = ['l', 'n', 's'] # choose whether the next element of the password will be a letter, number, or symbol
cases = ['upper', 'lower']

def create_password():

	pass_length, num_letters, num_symbols, num_numbers = 6, 0, 0, 0

	def request(): # request parameters for the password

		nonlocal pass_length, num_letters, num_symbols, num_numbers

		specify = int(input('Would you like to choose the parameters for your password? (Enter 0 for No or 1 for Yes): '))
		if specify:
			pass_length = int(input('How long would you like your password to be? (Minimum 6 characters, Maximum 16 characters): ')) # determine password length
			if pass_length < 6:
				pass_length = int(input('Password too short! How long would you like your password to be?: '))
			elif pass_length > 16:
				pass_length = int(input('Password too long! How long would you like your password to be?: '))
			num_letters = int(input('How many letters would you like in your password?: '))
			num_symbols = int(input('How many symbols would you like in your password?: '))
			num_numbers = int(input('How many numbers would you like in your password?: '))
		else:
			total = 6
			while total > 0:
				element_type = random.choice(choices)
				incrementation = random.choice(list(range(1, total + 1)))
				if element_type == 'l' and total > 0:
					num_letters += incrementation
				elif element_type == 'n' and total > 0:
					num_numbers += incrementation
				elif element_type == 's' and total > 0:
					num_symbols += incrementation
				total -= incrementation
		return generator(pass_length, num_letters, num_symbols, num_numbers)

	def generator(length, letters, symbols, numbers):
		if not letters + symbols + numbers == length:
			print('Parameters do not sum to your specified length! Try again.')
			request()
		password = ''
		while len(password) < length:
			element = random.choice(choices)
			if element == 'l' and letters > 0:
				case = random.choice(cases)
				if case == 'upper':
					password += random.choice(uppercase)
				else:
					password += random.choice(lowercase)
				letters -= 1
			elif element == 'n' and numbers > 0:
				password += str(random.choice(all_numbers))
				numbers -= 1
			elif element == 's' and symbols > 0:
				password += str(random.choice(password_symbols))
				symbols -= 1
		return password

	return request()
