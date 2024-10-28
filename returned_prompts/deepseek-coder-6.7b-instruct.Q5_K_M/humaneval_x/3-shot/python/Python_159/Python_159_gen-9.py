    eaten = number
    left = remaining
    
    if need < remaining:
        eaten += need
        left -= need
    else:
        eaten += remaining
        left = 0
        
    return [eaten, left]


