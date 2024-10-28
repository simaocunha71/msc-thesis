
    def sort_third(l: list):
        sorted_lst = sorted(l[i] for i in range(len(l)) if i % 3 == 0)
        res = []
        for i in range(len(l)):
            if i % 3 == 0:
                res.append(sorted_lst.pop(0))
            else:
                res.append(l[i])
        return res

    print(sort_third([1, 2, 3]))  # [1, 2, 3]
    print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]


if __name__ == '__main__':
    import doctest
    doctest.testmod()


This function works by first creating a sorted list of the elements at the indices divisible by 3. Then, it creates a new list where for each index, if it is divisible by 3, it takes the next element from the sorted list (and removes it from the sorted list), otherwise it takes the element from the original list.

The function uses a list comprehension to create the sorted list of elements at the indices divisible by 3, and the pop method to remove elements from the sorted list as they are used.

The function uses the % operator to check if an index is divisible by 3, and the append method to add elements to the new list.

The function uses the sorted function to create the sorted list of elements at the indices divisible by 3. The sorted function returns a new sorted list from the elements of the original list, and does not modify the original list.

The function uses the len function to get the length of the original list, and the range function to create a sequence of indices from 0 to the length of the original list.

The function uses the if else statement to check if an index is divisible by 3, and the append method to add elements to the new list.

The function uses the doctest module to test the function with the provided examples. The test function returns a TestResults object that has the following attributes:

- run: