def perfect_squares(a,b):
    # write your code here
    result = []
    for i in range(a,b+1):
        if i**0.5 == int(i**0.5):
            result.append(i)
    return result
