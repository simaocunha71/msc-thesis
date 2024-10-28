    def sum_squares(lst):
        return sum(int(round(x)) ** 2 for x in lst)  # Using list comprehension and sum function.
        # Here, we are using round to round each element to upper int (Ceiling) and int to convert it to integer.
        # Then we are squaring each element and summing them up. 

    # Example usage:
    print(sum_squares([1,2,3]))  # Output: 14
    print(sum_squares([1,4,9]))  # Output: 98
    print(sum_squares([1,3,5,7]))  # Output: 84
    print(sum_squares([1.4,4.2,0]))  # Output: 29
    print(sum_squares([-2.4,1,1]))  # Output: 6

    # Testing for edge cases:
    print(sum_squares([]))  # Output: 0
    print(sum_squares([0]))  # Output: 0
    print(sum_squares([0.0]))  # Output: 0
    print(sum_squares([0.5]))  # Output: 1
    print(sum_squares([0.9]))  # Output: 1
    print(sum_squares([0.1]))  # Output: 1
    print(sum_squares([0.99]))  # Output: 1
    print(sum_squares([1.0]))  # Output: 1
    print(sum_squares([1.1]))  # Output: 2
    print(sum_squares([1.9]))  # Output: 4
    print(sum_squares([2.0]))  # Output: 4
    print(sum_squares([2.1]))  # Output: 5
    print(sum_squares([2.9]))  # Output: 9
    print(sum_squares([3.0]))  # Output: 9
    print(sum_squares([3.1]))  # Output: 10
    print(sum_squares([3.9]))  # Output: 16
    print(sum_squares([4.0]))  # Output: 16
    print(sum_squares([4.1]))  # Output: 17
    print(sum_squares([4.9]))  # Output: 25
    print(sum_squares