"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
from typing import List

def sort_by_second(data: List[List[str, int]]) -> None:
    """Sort a list of tuples using the second value."""
    for i in range(len(data)):
        temp = data[i]
        data.pop(i)
        
        #sort the whole array
        j=0
        while j< len(data):
            if int(temp[1])>int(data[j][1]):
                temp = data[j+1:j+2]
                data[j]=data[j+1]+data[j+2]
                j+=2
            else:
                break
        data.insert(i,temp)
    print("sorted list is",data)