    def total_match(lst1, lst2):
        sum1 = sum(len(item) for item in lst1)
        sum2 = sum(len(item) for item in lst2)
        
        if sum1 < sum2:
            return lst1
        elif sum1 > sum2:
            return lst2
        else:
            return lst1
    # test the function
    print(total_match([], []))  # ➞ []
    print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ➞ ['hI', 'Hi']
    print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ➞ ['hi', 'admin']
    print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ➞ ['hI', 'hi', 'hi']
    print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ➞ ['4']
    print(total_match(['hi', 'admin'], ['hi', 'hi', 'hi', 'hi', 'hi']))  # ➞ ['hi', 'admin']  # this case is not handled in the function
    print(total_match(['hi', 'admin'], ['hi', 'hi', 'hi', 'hi']))  # ➞ ['hi', 'admin']  # this case is not handled in the function
    print(total_match(['hi', 'admin'], ['hi', 'hi', 'hi', 'hi', 'hi', 'hi']))  # ➞ ['hi', 'admin']  # this case is not handled in the function

