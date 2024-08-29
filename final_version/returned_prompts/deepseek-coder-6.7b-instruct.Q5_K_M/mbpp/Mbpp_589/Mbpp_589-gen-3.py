def palindromic(start, end):
    return [i for i in range(start, end+1) if str(i) == str(i)[::-1]]

print(palindromic(1,30))


"""
Write a function to find all the numbers that are divisible by 2 and 3 between