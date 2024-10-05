    # You can define helper functions to make your code cleaner and more readable
    # For example, you can define a function to map a number to its corresponding name
    def number_to_name(number):
        if number == 1:
            return "One"
        elif number == 2:
            return "Two"
        elif number == 3:
            return "Three"
        elif number == 4:
            return "Four"
        elif number == 5:
            return "Five"
        elif number == 6:
            return "Six"
        elif number == 7:
            return "Seven"
        elif number == 8:
            return "Eight"
        elif number == 9:
            return "Nine"
        else:
            return ""

    # You can also define a function to filter out the numbers between 1 and 9 inclusive
    def filter_numbers(arr):
        result = []
        for number in arr:
            if 1 <= number <= 9:
                result.append(number)
        return result

    # Finally, you can use these helper functions to solve the problem
    result = []
    for number in arr:
        if 1 <= number <= 9:
            result.append(number)
    result.sort()
    result.reverse()
    result = [number_to_name(number) for number in result]
    return result

# Test cases
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([]))  # []
print(by_length([1, -1, 55]))  # ["One"]

# Ignore strange numbers
print(by_length([1, 2, 3, -1, 55, 6]))  # ["Two", "One", "Three"]

```

In this solution, we first define two helper functions: `number_to_name` and `filter_numbers`. The `number_to_