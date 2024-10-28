    def countOnes(n):
        bin_str = bin(n)[2:]
        return bin_str.count('1')

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
    return sorted(arr, key=cmp_to_key(lambda a, b: (countOnes(b), -a)))



