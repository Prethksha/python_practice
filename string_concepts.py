# Program to understand string concepts in Python

# 1. Creation of a string
my_string = "Hello, World!"
print(f"Original string: {my_string}") # Using f-string formatting

# 2. Accessing characters using indexing (0-based)
first_char = my_string[0]
print(f"First character: {first_char}")

# 3. Getting the length of a string
string_length = len(my_string)
print(f"Length of the string: {string_length}")

# 4. Concatenation (joining strings)
another_string = " How are you?"
combined_string = my_string + another_string
print(f"Concatenated string: {combined_string}")


substring = my_string[0:5]
print(f"Sliced substring: {substring}")
