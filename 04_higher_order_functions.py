# Higher order functions

from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5;

def sum_two_values(first_value, second_value):
    print(first_value)
    return first_value + second_value

def sum_two_values_and_add_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_one(5, 2, sum_one))

# Closures

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(2)
print(add_closure(5))
sum_ten(4)
print(add_closure(3))
sum_ten(4)
print(add_closure(6))

# Map
print("-" * 30)
numbers = [2, 5, 10, 21]

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))

# Filter
some_numbers = [7, 1, 43, 21, 45, 35, 32, 62, 4]

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, some_numbers)))
print(list(filter(lambda number: number > 10, some_numbers)))

# Reduce

print(reduce(sum_two_values, some_numbers))