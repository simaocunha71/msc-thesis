def by_length(arr):
    dic = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    arr = sorted([i for i in arr if 1 <= i <= 9])
    arr.reverse()
    return [dic[i] for i in arr]

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1 , 55]))