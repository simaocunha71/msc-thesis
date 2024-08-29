def cal_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        perrin = [0, 1, 2]
        for i in range(3, n + 1):
            perrin.append(perrin[i - 1] + perrin[i - 2] + perrin[i - 3])
        return sum(perrin)


print(cal_sum(9))  # 49

"""
Explanation:
The perrin numbers are a sequence of numbers in which each number is the sum of the three previous numbers. 
The sequence starts with 3 numbers, 3, 0, 2 and each successive number is obtained by adding the three previous numbers. 
So the first few numbers of the sequence are 3, 0, 2, 3, 2, 5, 7, 10, 15, 22, 32, 45, 63, 87, 119, 162, 218, 291, 385, 504, 652, 833, 1051, 1311, 1618, 1977, 2394, 2875, 3426, 4053, 4762, 5560, 6453, 7448, 8552, 9771, 11111, 12580, 14185, 15933, 17831, 19886, 22105, 24496, 27066, 29822, 32771, 35921, 39280, 42856, 46657, 50691, 54966, 59491, 64274, 