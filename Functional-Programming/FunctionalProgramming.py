def add_two_numbers(a: int or float, b: int or float) -> int or float:
    """This function adds two numbers (not much more to say...)"""
    return a + b

def multiply_two_numbers(a: int or float, b: int or float) -> int or float:
    """This function multiplies two numbers (a bit fancier than adding, but not by much)"""
    return a * b

def my_map(arr, func):
    """An implementation of the map() function, which takes an iterable (e.g. array) and
    some function that acts on each element in the collection. This function does not modify
    the existing iterable, but creates a new one with modified elements."""
    if len(arr) == 0:
        return []
    return [func(arr[0])] + my_map(arr[1:], func)

def my_filter(arr, func):
    """An implementation of the filter() function, which takes an iterable and some conditional
    statement that acts on each element to determine whether the element should be present in the
    newly generated returned list."""
    if len(arr) == 0:
        return []
    rv = [arr[0]] + my_filter(arr[1:], func) if func(arr[0]) else my_filter(arr[1:], func)
    return rv

def my_reduce(arr, func):
    """An implementation of the reduce() function, which takes an iterable and applies some
    function on it that reduces it into a single variable. An example would be an array of 10
    numbers and the sum() function, which will reduce the list into a sum of the numbers in the
    iterable."""
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return func(arr[0], my_reduce(arr[1:], func))

def bubble_sort_iterative(iterable: list) -> list:
    """An implementation of the bubble sort algorithm used to sort elements in an iterable. This
    implementation uses iteration, and is not functional. It repeatedly modifies data over iterations
    (violating the principle of immutability), which in turn violates the principles of pure functions
    (which impose immutability and no side effects) and lazy evaluation, as data mutability and side effects
    yield lazy evulation unusable.
    """
    

def bubble_sort_recursive(iterable: list) -> list:
    """A recursive implementation of the bubble sort algorithm. Since this implementation uses recursion,
    does not mutate data and produces no side effects. Therefore this iplementation is functional!"""
    pass


def main():
    list = [1,2,3,4,5]
    """LAMBDA EXERCISES:
    1. Write a lambda function that adds 10 to each element in the above list
    2. Write a lambda function that squares each element in the above list
    3. Write a lambda function that raises each element to 3rd power
    4. Write a lambda function that raises each element to the nth power"""

if __name__ == '__main__':
    main()