def find_Rotations(s):
    # length of the string
    n = len(s)
    
    # creating a string by concatenating the string with itself
    temp = s + s
    
    # storing the length of the string in a variable
    l = len(temp)
    
    # creating a list to store the possible rotations of the string
    rotations = []
    
    # finding all the rotations of the string
    for i in range(1, l):
        if i % n == 0:
            rotations.append(temp[i:i+n])
    
    # initializing the minimum rotations to infinity
    min_rotations = float('inf')
    
    # finding the minimum number of rotations
    for rotation in rotations:
        if rotation == s:
            min_rotations = min(min_rotations, rotations.index(rotation))
            
    # returning the minimum number of rotations
    return min_rotations if min_rotations != float('inf') else -1

# testing the function
print(find_Rotations("aaaa")) # should return 1

