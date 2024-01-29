# A key-value pair is a set of values associated with each other. 
# When you provide a key, Python returns the value associated with that key. 
# Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.

emp = {'name': 'ali', 'age': '27'}
print(f"\nemp dictionary: {emp}")

# storing value of a key in a variable
emp_age = emp['age']
print(f"employe age is: {emp_age}")

# adding new keyvalue to the dictionary
emp['designation'] = 'driver'
print(f"updated emp dictionary: {emp}")

# modifying values of in a dictionary
emp['age'] = '28'
print(f"updated emp age is: {emp['age']}")
print("designation added to dictionary:",emp)

# deleting key-value pair in dictionary
del (emp['age'])
print(f"dictionary after deleting employe_age: {emp}")
