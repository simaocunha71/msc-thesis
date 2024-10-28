    def helper(lst1, lst2):
        if len(lst1) != len(lst2):
            return False
        odd_lst1 = [num for num in lst1 if num % 2 != 0]
        odd_lst2 = [num for num in lst2 if num % 2 != 0]
        return len(odd_lst1) <= len(odd_lst2)

    return 'YES' if helper(lst1, lst2) else 'NO'


