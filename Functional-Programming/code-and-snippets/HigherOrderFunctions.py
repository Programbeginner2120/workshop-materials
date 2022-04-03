def add_two_numbers(x: int, y: int) -> int:
    return x + y

a, b = 2, 3
first_class_function = add_two_numbers
print(first_class_function(a,b)) # prints 5
print(add_two_numbers(a,b)) # prints 5


def add_four_numbers(a, b, c, d):
    return a+b+c+d

def add_four_numbers_higher_order(first_class_func: object, a, b, c, d) -> int:
    return first_class_func(a,b) + first_class_func(c,d)

c, d = 4, 5
print(add_four_numbers(a, b, c, d)) # prints 14
print(add_four_numbers_higher_order(first_class_function, a, b, c, d)) # prints 14


