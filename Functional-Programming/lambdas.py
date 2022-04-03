# def my_map(arr, func):
#     result = []
#     for elem in arr:
#         result.append(func(elem))
#     return result

# def my_filter(arr, func):
#     result = []
#     for elem in arr:
#         if func(elem):
#             result.append(elem)
#     return result

def my_map(arr, func):
    if len(arr) == 0:
        return []
    return [func(arr[0])] + my_map(arr[1:], func)

def my_filter(arr, func):
    if len(arr) == 0:
        return []
    rv = [arr[0]] + my_filter(arr[1:], func) if func(arr[0]) else my_filter(arr[1:], func)
    return rv

def my_reduce(arr, func):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return func(arr[0], my_reduce(arr[1:], func))


array = [1,2,3,4,5]

add_two = lambda x: x+2
rv = my_map(array, add_two)
print(rv)

condition = lambda x: x <= 3
rv = my_filter(array, condition)
print(rv)

multiply = lambda x, y: x*y
rv = my_reduce([1,2,4], multiply)
print(rv)


