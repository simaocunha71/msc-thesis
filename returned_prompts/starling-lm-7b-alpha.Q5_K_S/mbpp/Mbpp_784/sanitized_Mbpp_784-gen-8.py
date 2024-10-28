def mul_even_odd(list):
    evens = []
    odds = []
    for i in range(len(list)):
        if i % 2 == 0:
            evens.append(list[i])
        else:
            odds.append(list[i])
    return evens[0] * odds[0]
list = [1,3,5,7,4,1,6,8]