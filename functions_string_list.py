# Function to calculate the sum of a list using the built-in function sum()
def calculate_sum(numbers):
 total = sum(numbers)
 return total
# Function to find the length of a string using the built-in function len()
def find_string_length(text):
 length = len(text)
 return length
# Function to convert a string to uppercase using the built-in function upper()
def convert_to_uppercase(text):
 uppercase_text = text.upper()
 return uppercase_text

 # Example 2: Find the length of a string
 input_string = input("Enter a string: ")
 string_length = find_string_length(input_string)
 print(f"The length of the string is: {string_length}")
 # Example 3: Convert a string to uppercase
 input_text = input("Enter a string to convert to uppercase: ")
 uppercase_result = convert_to_uppercase(input_text)
 print(f"The string in uppercase is: {uppercase_result}")