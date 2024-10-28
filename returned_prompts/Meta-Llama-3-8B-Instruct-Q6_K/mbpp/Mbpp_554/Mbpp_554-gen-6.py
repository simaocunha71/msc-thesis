def Split(lst):
    return [i for i in lst if i % 2 != 0]
"""
This function uses list comprehension to create a new list that includes only the odd numbers from the input list. The condition i % 2 != 0 checks if a number is odd, and if it is, it's included in the new list. 
The unit test provided, `assert Split([1,2,3,4,5,6]) == [1,3,5]`, shows that the function should return a list of odd numbers from the input list. 
"""



