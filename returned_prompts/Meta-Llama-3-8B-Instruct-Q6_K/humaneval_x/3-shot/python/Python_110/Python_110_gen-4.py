    def exchange(lst1, lst2):
        if any(num % 2 != 0 for num in lst1):
            return "NO"
        return "YES"


