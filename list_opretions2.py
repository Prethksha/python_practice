# A list of fruits.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# 1. Accessing elements using positive indices
first_fruit = fruits[0] 
second_fruit = fruits[1]
last_fruit = fruits[4]   

print(f"The first fruit is: {first_fruit}")
print(f"The second fruit is: {second_fruit}")
print(f"The last fruit is: {last_fruit}")
# 2. Accessing elements using negative indices (from the end of the list)
last_fruit_neg = fruits[-1]
second_last_fruit = fruits[-2]

print(f"\nThe last fruit using negative indexing is: {last_fruit_neg}")
print(f"The second to last fruit is: {second_last_fruit}")

# 3. Iterating through a list and accessing both index and value
print("\nIterating through the list:")
for index, value in enumerate(fruits):
    print(f"Index: {index}, Value: {value}")

# 4. An example of an "IndexError" (trying to access an index that does not exist)
try:
    non_existent = fruits[10]
except IndexError as e:
    print(f"\nCaught an error: {e}")
