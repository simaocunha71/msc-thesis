    def add(lst):
        return sum(x for x in lst if x % 2 == 0 and lst.index(x) % 2 != 0)
    # or
    def add(lst):
        result = 0
        for i, x in enumerate(lst):
            if x % 2 == 0 and i % 2 != 0:
                result += x
        return result
    # or
    def add(lst):
        return sum(x for i, x in enumerate(lst) if x % 2 == 0 and i % 2 != 0) 
    # or
    def add(lst):
        return sum(x for i, x in enumerate(lst) if i % 2 != 0 and x % 2 == 0) 
    # or
    def add(lst):
        return sum([x for x in lst if x % 2 == 0 and lst.index(x) % 2 != 0])
    # or
    def add(lst):
        result = 0
        for i in range(0, len(lst)):
            if i % 2 != 0 and lst[i] % 2 == 0:
                result += lst[i]
        return result
    # or
    def add(lst):
        return sum([x for i, x in enumerate(lst) if i % 2 != 0 and x % 2 == 0]) 
    # or
    def add(lst):
        return sum([x for i in range(0, len(lst)) if i % 2 != 0 and lst[i] % 2 == 0]) 
    # or
    def add(lst):
        result = 0
        for i in range(0, len(lst)):
            if i % 2 == 0 and lst[i] % 2 != 0:
                result += lst[i]
        return result
    # or
    def add(lst):
        return sum([x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 != 0]) 
    # or
    def add(lst):
        return sum([x for i in range(0, len(lst)) if i % 2 == 0 and lst[i] % 2 != 0]) 
    # or
    def add(lst):
        result = 0
        for i, x in enumerate(lst):
            if i % 2 != 