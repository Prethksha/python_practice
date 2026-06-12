# Program to calculate the average of five numbers using input() and type conversion
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
num5 = float(input("Enter the fifth number: "))

# 2. Calculate the sum of the five numbers
total_sum = num1 + num2 + num3 + num4 + num5

# 3. Calculate the average by dividing the sum by the count of numbers (which is 5)
average = total_sum / 5

# 4. Display the result to the user
#    We use an f-string for a clean output.
print(f"\nThe numbers entered are: {num1}, {num2}, {num3}, {num4}, and {num5}")
print(f"The sum of the numbers is: {total_sum}")
print(f"The average of the five numbers is: {average}")


