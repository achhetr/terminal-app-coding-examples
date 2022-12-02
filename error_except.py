# errors and exception

# while True: print("yes")

# define name:
#   print('define')


# programming

# compiling the document
# execution

# exception

# print(100 / 0)

# rule 1 -> we never skip any compilations errors
# rule 2 -> we will only users exception

# try/catch block
# user_input = input("Enter your fav number!") # api 0,number alphanumeric

# try:
#   print(100 / int(user_input))
# except ZeroDivisionError:
#   print('your fav number cannot be ZERO')
# except ValueError:
#   print('please only enter numbers with base 10')
# else:
#   print('you guessed the right number')
# finally:
#   print('I will always exceute')


user_input = input("Enter your fav number!") # api 0,number alphanumeric

try:
  print(100 / int(user_input))
except ZeroDivisionError:
  print('your fav number cannot be ZERO')
except ValueError:
  print('please only enter numbers with base 10')
else:
  print('you guessed the right number')
finally:
  print('I will always exceute')

class UserDepositedLessThanTenDollars(Exception):
  pass

# raise UserDepositedLessThanTenDollars # raise specific exception

# does return something but it is acceptable
# shop user to pay using eftpos more 10 dollars
# raise UserDepositedLessThanTenDollars

# class UserDepositedLessThanTenDollars(Exception):
#   pass
