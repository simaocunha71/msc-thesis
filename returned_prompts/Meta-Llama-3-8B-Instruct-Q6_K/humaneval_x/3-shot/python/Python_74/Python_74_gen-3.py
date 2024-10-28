    def total_match(lst1, lst2):
        total_chars1 = sum(len(s) for s in lst1)
        total_chars2 = sum(len(s) for s in lst2)
        
        if total_chars1 < total_chars2:
            return lst1
        elif total_chars2 < total_chars1:
            return lst2
        else:
            return lst1
    # Test cases
    print(total_match([], []))  # []
    print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ['hI', 'Hi']
    print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ['hi', 'admin']
    print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ['hI', 'hi', 'hi']
    print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ['4']  # Test case added by me
    # I added the last test case as the original one was missing it. The function now correctly handles the test case where one of the input lists contains a single element.