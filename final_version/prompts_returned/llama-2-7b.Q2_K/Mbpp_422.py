"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""

def find_Average_Of_Cube(n):
    def first_index_and_cubed_number_of_first_n():
        #Write your code here.
        return [i**3 for i in range(1, n+1)]
    
    #Write your code here.
    A = list(map(list, zip(*first_index_and_cubed_number_of_first_n())))
    A = sum(A)/len(A) 
    
    return A