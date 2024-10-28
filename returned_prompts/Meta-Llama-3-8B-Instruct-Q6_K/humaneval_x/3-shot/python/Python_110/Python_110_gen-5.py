    def exchange(lst1, lst2):
        odd_elements_in_lst1 = [num for num in lst1 if num % 2 != 0]
        odd_elements_in_lst2 = [num for num in lst2 if num % 2 != 0]
        
        if len(odd_elements_in_lst1) > len(odd_elements_in_lst2):
            return "NO"
        else:
            for odd_num in odd_elements_in_lst1:
                if odd_num not in odd_elements_in_lst2:
                    return "NO"
            return "YES"


