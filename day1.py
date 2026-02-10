#variable 
first_name ="Mahnaj"
print(first_name)
#f-string = format string
print(f"Hello, {first_name}!")
#input function
name = input("What is your name? ")
print(f"Hello, {name}!")
#data types
age = 25 #integer
height = 5.9 #float
is_student = True #boolean
print(f"Age: {age}, Height: {height}, Is Student: {is_student}")
#type conversion
age_str = str(age) #convert integer to string
print(f"Age as string: {age_str}")
height_int = int(height) #convert float to integer
print(f"Height as integer: {height_int}")
#arithmetic operations
num1 = 10
num2 = 5
sum_result = num1 + num2
print(f"Sum: {sum_result}")
difference = num1 - num2
print(f"Difference: {difference}")
product = num1 * num2
print(f"Product: {product}")
quotient = num1 / num2
print(f"Quotient: {quotient}")
#logical operations
is_adult = age >= 18
print(f"Is adult: {is_adult}")
is_tall = height > 6.0
print(f"Is tall: {is_tall}")
is_student_and_adult = is_student and is_adult
print(f"Is student and adult: {is_student_and_adult}")
#comments
# This is a single-line comment
"""This is a multi-line comment
that spans multiple lines."""
print("Comments are ignored by the interpreter.")
#print function
print("This is a print statement.")
print("You can print variables too:", first_name, age)
#escape sequences
print("Hello,\nWorld!") # New line
print("Hello,\tWorld!") # Tab
print("He said, \"Hello!\"") # Double quote
print('It\'s a beautiful day!') # Single quote
#string concatenation
greeting = "Hello, " + first_name + "!"
print(greeting)
#string formatting
formatted_greeting = "Hello, {}!".format(first_name)
print(formatted_greeting)
#f-string formatting
f_string_greeting = f"Hello, {first_name}!"
print(f_string_greeting)
#string methods
print(first_name.upper()) # Convert to uppercase
print(first_name.lower()) # Convert to lowercase
print(first_name.capitalize()) # Capitalize the first letter
print(first_name.replace("a", "o")) # Replace 'a' with 'o'
#string slicing
print(first_name[0]) # First character
print(first_name[1:4]) # Characters from index 1 to 3
print(first_name[:3]) # First three characters
print(first_name[3:]) # Characters from index 3 to the end
#string length
print(len(first_name)) # Length of the string
#string concatenation with f-string
full_name = f"{first_name} Smith"
print(full_name)
#string formatting with f-string
age_message = f"{first_name} is {age} years old."
print(age_message)
#string formatting with format method
age_message_format = "{} is {} years old.".format(first_name, age)
print(age_message_format)
#string formatting with % operator
age_message_percent = "%s is %d years old." % (first_name, age)
print(age_message_percent)
#string formatting with f-string and expressions
next_year_age = f"Next year, {first_name} will be {age + 1} years old."
print(next_year_age)
#string formatting with format method and expressions
next_year_age_format = "{} will be {} years old next year.".format(first_name, age + 1)
print(next_year_age_format)
#string formatting with % operator and expressions
next_year_age_percent = "%s will be %d years old next year." % (first_name, age + 1)
print(next_year_age_percent)
