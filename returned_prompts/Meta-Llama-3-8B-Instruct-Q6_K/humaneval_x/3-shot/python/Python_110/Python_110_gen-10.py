    def exchange(lst1, lst2):
        odd_in_lst1 = [i for i in lst1 if i % 2 != 0]
        odd_in_lst2 = [i for i in lst2 if i % 2 != 0]

        if len(odd_in_lst1) > len(odd_in_lst2):
            return "NO"
        elif len(odd_in_lst1) < len(odd_in_lst2):
            return "NO"
        else:
            return "YES"


