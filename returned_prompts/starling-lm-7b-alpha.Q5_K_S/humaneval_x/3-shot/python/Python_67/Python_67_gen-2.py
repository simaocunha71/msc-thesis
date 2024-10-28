    a,o = [int(i) for i in s.split() if i != 'and']
    total_fruits = n
    mango = total_fruits - a - o
    return mango


