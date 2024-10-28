    # Write your code here
    def exchange(lst1, lst2):
        odd_lst1 = []
        for i in lst1:
            if i % 2 != 0:
                odd_lst1.append(i)
        odd_lst2 = []
        for i in lst2:
            if i % 2 != 0:
                odd_lst2.append(i)

        if len(odd_lst1) > len(odd_lst2):
            return 'NO'
        else:
            for i in odd_lst1:
                if odd_lst2.count(i) > 0:
                    odd_lst2.remove(i)
            if len(odd_lst2) == 0:
                return 'YES'
            else:
                return 'NO'


# Driver Code
lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 3, 4]
print(exchange(lst1, lst2))





lst1 = [1, 2, 3, 4]
lst2 = [1, 5, 3, 4]
print(exchange(lst1, lst2))



















































































































































































































