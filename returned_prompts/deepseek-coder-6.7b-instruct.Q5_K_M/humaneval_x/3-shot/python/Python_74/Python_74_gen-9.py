    def total_match(lst1, lst2):
        sum_lst1 = sum([len(i) for i in lst1])
        sum_lst2 = sum([len(i) for i in lst2])
        if sum_lst1 < sum_lst2:
            return lst1
        else:
            return lst2
    print(total_match(['hi', 'admin'], ['hI', 'Hi']))
    print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
    print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
    print(total_match(['4'], ['1', '2', '3', '4', '5']))
    '''
    The function works by first calculating the total number of characters in each list using a list comprehension. It then compares these totals and returns the list that has a smaller total. If the totals are equal, it returns the first list.
    '''

