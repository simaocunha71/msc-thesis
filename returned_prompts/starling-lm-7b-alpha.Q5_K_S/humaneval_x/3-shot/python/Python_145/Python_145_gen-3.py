    def sum_of_digits(num):
        return sum(map(int, str(num)))

    def cmp_to_key(mycmp):
        'Convert a cmp= function into a key= function'
        class K:
            def __init__(self, obj, *args):
                self.obj = obj

            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0

            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0

            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0

        return K

    return sorted(nums, key=cmp_to_key(lambda a, b: (sum_of_digits(a), -a) < (sum_of_digits(b), b)))


