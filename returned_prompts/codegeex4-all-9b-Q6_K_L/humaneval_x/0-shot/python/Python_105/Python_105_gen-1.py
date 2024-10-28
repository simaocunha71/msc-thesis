def by_length(arr):
    dic = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    return [dic[i] for i in sorted([i for i in arr if 1<=i<=9])[::-1]]

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([1, -1 , 55]))
print(by_length([]))