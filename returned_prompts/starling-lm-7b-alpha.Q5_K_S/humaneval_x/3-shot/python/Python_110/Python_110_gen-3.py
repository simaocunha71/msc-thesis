    def exchange(lst1, lst2):
        odd_count = sum(1 for i in lst1 if i % 2 != 0)
        even_count = sum(1 for i in lst2 if i % 2 == 0)
        return "YES" if odd_count <= even_count else "NO"


