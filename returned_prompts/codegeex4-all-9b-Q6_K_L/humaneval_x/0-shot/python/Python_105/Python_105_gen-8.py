def by_length(arr):
    nums = sorted([i for i in arr if 1 <= i <= 9], reverse=True)
    nums = [str(i) for i in nums]
    nums = [i.replace("1", "One") for i in nums]
    nums = [i.replace("2", "Two") for i in nums]
    nums = [i.replace("3", "Three") for i in nums]
    nums = [i.replace("4", "Four") for i in nums]
    nums = [i.replace("5", "Five") for i in nums]
    nums = [i.replace("6", "Six") for i in nums]
    nums = [i.replace("7", "Seven") for i in nums]
    nums = [i.replace("8", "Eight") for i in nums]
    nums = [i.replace("9", "Nine") for i in nums]
    return nums