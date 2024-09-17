```
def is_Sub_Array(sub, main):
    try:
        for i in range(len(main)-len(sub)+1):
            if main[i:i+len(sub)] == sub:
                return True
        return False
    except TypeError:
        return False
``` 

This function checks if the sub list is a sublist of the main list. If the sub list is found in the main list, it returns True. If not, it returns False. 

The function uses a try-except block to handle the case where the input is not a list. 

The unit test `assert is_Sub_Array([1,4,3,5],[1,2]) == False` ensures that the function correctly returns False for non-sublist inputs. 

This function is case sensitive and considers order. It will return False if the sublist is not found in the main list, even if the elements are the same but in different order. For example, `[1,2,3]` is not a sublist of `[3,1,2]`. 

This function has a time complexity of O(n*m) where n is the length of the main list and m is the length of the sub list. This is because it potentially needs to iterate over the main list m times. 

It has a space complexity of O(1) as it only uses a constant amount of space to store the variables and does not use any data structures that scale with the input size. 

Note: This function does not check for duplicates in the main list. If the main list contains duplicate elements and the sub list contains the same element multiple times, it will still consider the sub list as a sublist. For example, `[1,2,2,3]` is a sublist of `[1,2,2,2,3]`. If you want to avoid this, you can modify the function to keep track of the count of each element in the main list and the sub list. If the counts do not match, return False. 

Also, this function does not check for order in the main list. If the main list contains duplicate elements and the sub list contains the same element multiple times, it will still consider the sub list as a sublist. For example, `[1,2,2,3]` is a sublist of `[1,2,2,3,2]`. If you want to avoid this, you can modify the function to keep track of the order of elements in the main list and the sub list. If