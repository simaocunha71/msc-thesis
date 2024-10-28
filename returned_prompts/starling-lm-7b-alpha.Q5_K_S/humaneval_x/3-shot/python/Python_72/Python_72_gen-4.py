    def will_it_fly(q,w):
        # Check if the list is palindromic
        for i in range(len(q)//2):
            if q[i] != q[len(q)-i-1]:
                return False
        # Check if the sum of the list elements is less than or equal to the maximum weight
        if sum(q) <= w:
            return True
        return False


