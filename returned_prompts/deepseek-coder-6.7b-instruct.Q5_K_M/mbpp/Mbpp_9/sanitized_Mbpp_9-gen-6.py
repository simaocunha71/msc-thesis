def find_Rotations(s):
    n = len(s)
    temp = s + s
    rotations = []
    
    for i in range(1, n):
        if temp[i:i+n] == s:
            rotations.append(i)
    
    min_rotations = min(rotations)
    
    return min_rotations if min_rotations < n else -1