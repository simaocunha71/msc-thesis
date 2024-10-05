def by_length(arr):
    mapping = {
        0: "",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    result = []
    for num in sorted([x for x in arr if 1 <= x <= 9]):
        result.append(mapping[num])
    return result[::-1]

print(by_length([2, 1, 1, 4, 5, 8, 2, 3])) # ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([])) # []
print(by_length([1, -1 , 55])) # ["One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([9, 8, 7, 6, 5, 4, 3, 2, 1])) # ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]