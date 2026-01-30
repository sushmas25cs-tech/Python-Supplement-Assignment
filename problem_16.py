# Problem 16: Find the second largest number in a list
# Find and fix the error

# Problem 16: Find the second largest number in a list
# Find and fix the error

numbers = [45, 89, 12, 78, 34]

unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("Not enough unique elements")
else:
    unique_numbers.sort()
    second_largest = unique_numbers[-2]
    print(f"Second largest: {second_largest}")