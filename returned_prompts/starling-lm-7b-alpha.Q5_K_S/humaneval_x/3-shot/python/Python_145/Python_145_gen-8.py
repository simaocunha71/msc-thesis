    def sum_digits(n):
        result = 0
        while n > 0:
            result += n % 10
            n = n // 10
        return result

    def cmp_to_key(my_cmp):
        'Convert a cmp= function into a key= function'
        class K:
            def __init__(self, obj, *args):
                self.obj = obj

            def __lt__(self, other):
                return my_cmp(self.obj, other.obj) < 0

            def __gt__(self, other):
                return my_cmp(self.obj, other.obj) > 0

            def __eq__(self, other):
                return my_cmp(self.obj, other.obj) == 0

        return K

    return sorted(nums, key=cmp_to_key(lambda a, b: (sum_digits(a), id(a)) < (sum_digits(b), id(b))))


