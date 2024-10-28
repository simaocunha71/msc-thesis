
def exchange(lst1, lst2):
    odds = [x for x in lst1 if x % 2 != 0]
    evens = [x for x in lst2 if x % 2 == 0]
    if len(odds) > len(evens):
        return "NO"
    else:
        for i in range(len(odds)):
            lst1[odds[i]] = lst2[evens[i]]
        for i in range(len(lst1)):
            if lst1[i] % 2 != 0:
                return "NO"
        return "YES"






# Another approach
# def exchange(lst1, lst2):
#     odds = [x for x in lst1 if x % 2 != 0]
#     evens = [x for x in lst2 if x % 2 == 0]
#     if len(odds) > len(evens):
#         return "NO"
#     else:
#         for i in range(len(odds)):
#             lst1[odds[i]] = evens[i]
#         for i in range(len(lst1)):
#             if lst1[i] % 2 != 0:
#                 return "NO"
#         return "YES"





def test_exchange():
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert exchange([1, 2, 3, 4], [1, 2, 3, 5]) == "NO"
    assert exchange([1, 2, 3, 5], [1, 2, 3, 4]) == "NO"
    print("All test cases passed.")

if __name__ == "__main__":
    test_exchange()




# Made By Mostafa_Khaled
```
        
