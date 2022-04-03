import datetime

"""
Demonstration of factorial imperative vs. declarative
"""

def imperative_factorial(n: int) -> int:
    """Imperative calculation of n!, where the programmer explicitly 
    tells the computer what to do via iteration"""
    result = 1
    for num in range(1, n+1):
        result *= num
    return result


def declarative_factorial(n: int) -> int:
    """Declarative calculation of n!, where the programmer does not
    tell the computer what to do, but gives it basic rule(s) to
    follow and let's the computer determine how to calculate the result
    (in this case, it is calculated through recursion)."""
    if (n <= 1):
        return 1
    return n * declarative_factorial(n-1)


"""Showing the use of first-class functions and higher order functions via the get_compute_time() function"""

def get_average_compute_time(func, num_runs=1, n=1):
    result = 0
    for i in range(num_runs):
        start = datetime.datetime.now()
        func(n)
        end = datetime.datetime.now()
        result += (end - start).total_seconds() * 1000
    return result / num_runs


def fibonacci_1(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci_1(n-2) + fibonacci_1(n-1)


def fibonacci_2(n: int) -> int:
    fib_arr = [0, 1, 1]
    if n == 0:
        return fib_arr[0]
    if n <= 2:
        return fib_arr[1]
    for i in range(3, n+1):
        fib_arr.append(fib_arr[i-1] + fib_arr[i-2])
    return fib_arr[n]


def fib_testing():
    n = 11
    print(fibonacci_1(n))
    print(fibonacci_2(n))


def iter_length(arr):
    """Iterative length function"""
    i = 0
    temp_arr = arr
    while temp_arr != []:
        i = i + 1
        temp_arr = temp_arr[1:]
    return i


def rec_length(arr):
    """Recursive length function"""
    if arr == []:
        return 0
    temp_arr = arr[1:]
    return 1 + rec_length(temp_arr)


def length_testing():
    iter = [1,5,6,3,6]
    print(iter_length(iter))
    print(rec_length(iter))


def lambda_playground():
    # add a number to itself (double it)
    double = lambda x: x + x
    print(double(5))

    # add two numbers
    sum_two = lambda x, y: x + y
    print(sum_two(3, 4))

    # subtract two numbers
    subtract_two = lambda x, y: x - y
    print(subtract_two(3,4))

    # get the head of a list:
    get_head = lambda x: x[0]
    print(get_head([1,2,3,4,5]))

    # get the tail of a list:
    get_tail = lambda x: x[1:]
    print(get_tail([1,2,3,4,5]))

    # we can use these functions, get head and get tail
    # to get any element from our list!
    print(get_tail(get_head([1,2,3,4,5])))

    my_list = [1,2,3,4,5]
    """Challenge #1: Get the third element of my_list 
    using get_head and get_tail"""
    print(get_tail(get_tail(get_head(my_list))))

    # put your code here

    """Challenge #2: Get the second to last element of
    my_list"""

    # put your code here

    """Challenge #3: Create a lambda function that adds
    three numbers togehter"""

    # put your code here


# def iter_bubble_sort(list):
#     pass


# def rec_bubble_sort(list):
#     pass


# def bubble_sort_testing():
#     list = [9,2,88,1,7,2,5]
#     print(iter_bubble_sort(list))


def challenges():
    my_list = [1,2,3,4,5]
    """Challenge #1: Get the third element of my_list 
    using get_head and get_tail"""

    # put your code here

    """Challenge #2: Get the second to last element of
    my_list"""

    # put your code here

    """Challenge #3: Create a lambda function that adds
    three numbers togehter"""

    # put your code here

    """map(), filter() and reduce()"""

    my_list = [1,2,3,4,5]

    """Map Challenge #1: Use map to multiply each element by 2"""
    # put code here
    print(list(map(lambda x: x * 2, my_list)))

    """Map Challenge #2: Use map to raise each element to the third power"""
    # put code here
    print(list(map(lambda x: x ** 3, my_list)))
    """Map Challenge #3: Use map to divide each element by itself"""
    # put code here
    print(list(map(lambda x: x / x, my_list)))
    fruit_list = ["Apple", "Banana", "Pear", "Watermelon", "Cranberry"]

    """Filter Challenge #1: Use filter to take out all values in fruit_list length < 5"""
    # put code here
    print(list(filter(lambda x: len(x) >= 5, fruit_list)))

    """Filter Challenge #2: Use filter to remove all values in fruit_list with even length"""
    # put code here
    print(list(filter(lambda x: len(x) % 2 != 0, fruit_list)))

    """Filter Challenge #3: Use filter to remove all values in fruit_list that start with 'C'"""
    # put code here
    print(list(filter(lambda x: x[0] != 'C', fruit_list)))

    """Reduce Challenge #1: Use reduce to subtract all elements in my_list"""
    # put code here
    print(reduce(lambda x, y: x - y, my_list))

    """Reduce Challenge #2: Use reduce to multiply all elements in my_list"""
    # put code here
    print(reduce(lambda x, y: x * y, my_list))

    """Reduce Challenge #3: Use reduce to add all of the elements squared in the list"""
    # put code here
    print(reduce(lambda x, y: x + y**2, my_list))

    def lambda_playground():
    # add a number to itself (double it)
    double = lambda x: x + x
    print(double(5))

    # add two numbers
    sum_two = lambda x, y: x + y
    print(sum_two(3, 4))

    # subtract two numbers
    subtract_two = lambda x, y: x - y
    print(subtract_two(3,4))

    # get the head of a list:
    get_head = lambda x: x[0]
    print(get_head([1,2,3,4,5]))

    # # get the tail of a list:
    # get_tail = lambda x: x[1:]
    # print(get_tail([1,2,3,4,5]))

    # # we can use these functions, get head and get tail
    # # to get any element from our list!
    # print(get_tail(get_head([1,2,3,4,5])))

def main():
    imperative_call = imperative_factorial
    declarative_call = declarative_factorial

    imperative_result = get_average_compute_time(imperative_call, 100, n=30)
    declarative_result = get_average_compute_time(declarative_call, 100, n=30)

    print(f"Imperative Factorial Average: {'{:.3f}'.format(imperative_result)} milliseconds")
    print(f"Declarative Factorial Average: {'{:.3f}'.format(declarative_result)} milliseconds")

    #length_testing()

    lambda_playground()


if __name__ == "__main__":
    main()

# pure_variable = 100
# def pure_function(variable):
#     print(pure_variable)

# for i in range(100):
#     pure_function(pure_variable)


# impure_variable = 100
# def impure_function(variable):
#     print(variable)
#     return variable + 1

# for i in range(100):
#    impure_variable = impure_function(impure_variable)