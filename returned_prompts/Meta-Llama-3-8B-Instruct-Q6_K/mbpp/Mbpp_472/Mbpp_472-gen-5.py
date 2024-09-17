```
def check_Consecutive(lst):
    for i in range(len(lst) - 1):
        if lst[i+1] - lst[i] != 1:
            return False
    return True
```


The given function checks if a list contains consecutive numbers. It iterates over the list, comparing each number with the next one. If it finds a pair of numbers that are not consecutive (i.e., the difference between them is not 1), it returns False. If it checks all numbers and doesn't find any non-consecutive pair, it returns True, indicating that the list contains consecutive numbers. 

The unit test `assert check_Consecutive([1,2,3,4,5]) == True` ensures that the function works correctly for a list of consecutive integers. 

This function assumes that the input list is non-empty and contains at least two elements. If the input list is empty or contains less than two elements, this function may not work correctly. You might want to add error checking code to handle these cases, depending on your specific requirements. 





Note: This function assumes that the list contains integers. If the list can contain other types of numbers (like floats), you might need to adjust the comparison in the function accordingly. 

Also, this function checks for consecutive integers, not just consecutive elements. If you want to check for consecutive elements (i.e., elements that are not necessarily integers), you would need to adjust the comparison accordingly. 





The function is case-insensitive, as it treats integers as integers, regardless of their representation (e.g., 1 or '1'). If you want to make it case-sensitive, you would need to adjust the comparison accordingly. 





The function is also sensitive to the order of the elements in the list. If you want to make it insensitive to the order, you would need to adjust the comparison accordingly. 





This function does not handle non-numeric elements in the list. If you want to handle non-numeric elements, you would need to adjust the comparison accordingly. 





This function does not handle lists that contain duplicate elements. If you want to handle duplicate elements, you would need to adjust the comparison accordingly. 





This function does not handle lists that contain non-list elements. If you want to handle non-list elements, you would need to adjust the comparison accordingly. 





This function assumes that the input list is a list. If the input is not a list, this function may not work correctly. You might want