def sum_squares(lst):
    return sum(int(i) ** 2 for i in lst)
    # or
    # return sum(math.ceil(i) ** 2 for i in lst)
    # or
    # return sum(math.ceil(i) ** 2 for i in map(math.ceil, lst))
    # or
    # return sum(math.ceil(i) ** 2 for i in map(lambda x: math.ceil(x), lst))
    # or
    # return sum([math.ceil(i) ** 2 for i in lst])
    # or
    # return sum([math.ceil(i) ** 2 for i in map(math.ceil, lst)])
    # or
    # return sum(map(lambda x: math.ceil(x) ** 2, lst))



Here is the explanation:

1. The function sum_squares takes a list of numbers as input.
2. It uses a generator expression to iterate over each element in the list.
3. For each element, it rounds the element up to the nearest integer using the int() function.
4. It squares the rounded element and adds it to the sum.
5. The sum is then returned.

The int() function is used to round the element up to the nearest integer. This is because the problem statement asks for the sum of squared numbers, and int() rounds down to the nearest integer. By using int() instead of math.ceil(), we are effectively rounding up to the nearest integer.

The math.ceil() function is not necessary in this case, but it could be used if you wanted to explicitly round the element up to the nearest integer.

The map() function is not necessary in this case, but it could be used if you wanted to apply the int() or math.ceil() function to each element in the list.

The lambda function is not necessary in this case, but it could be used if you wanted to define a small anonymous function to use with the map() function.

The list comprehension is not necessary in this case, but it could be used if you wanted to create a new list with the rounded and squared elements, and then sum the list.