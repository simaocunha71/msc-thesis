def find_tuples(tuples, divisor):
    return [t for t in tuples if all(i % divisor == 0 for i in t)]