
def rotate_left(lst,n):
    return lst[n:]+lst[:n]

print(rotate_left([1,2,3,4,5],2)) #[3,4,5,1,2]

"""
Write a function to rotate a list to the right by n places. 
assert rotate_right([1,2,3,4,5],2)==[4,5,1,2,3]