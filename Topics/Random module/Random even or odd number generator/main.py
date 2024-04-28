import random


# Check if the number is even or odd
def even_or_odd(num):
    if num % 2:
        return 'Odd'
    return 'Even'


# Generate a random integer between 1 and 10 (inclusive)
random_int = random.randint(1, 10)

# Print the result
print(even_or_odd(random_int))
