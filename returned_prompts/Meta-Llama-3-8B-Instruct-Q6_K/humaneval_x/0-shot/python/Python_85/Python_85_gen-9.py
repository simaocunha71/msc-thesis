    def add(lst):
        return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 0)  # Pythonic one-liner
        # or
        # result = 0
        # for i, x in enumerate(lst):
        #     if i % 2 == 0 and x % 2 == 0:
        #         result += x
        # return result
        # or
        # return sum(x for x in lst if x % 2 == 0 and lst.index(x) % 2 != 0)  # not recommended due to O(n^2) time complexity


