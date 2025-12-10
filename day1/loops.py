numbers = [5, 8, 2, 9, 12, 7, 1, 10, 3, 6]

# Print even numbers

for n in numbers:
    if n % 2 == 0:
        print("Even:", n)

# Print the sum of all numbers

total = 0
for n in numbers:
    total += n
    print("Sum:", total)

# Find largest number manually (Without max())

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
print("Largest:", largest)

# Reverse list manually

reversed_list = []
for n in numbers:
    reversed_list = [n] + reversed_list
print("Reversed:", reversed_list)