    if not all(isinstance(i, int) for i in [x, y, z]):
        return False
    if x == y + z or x == z + y or y == x + z or y == z + x or z == x + y or z == y + x:
        return True
    return False
    # or return x+y==z or x+z==y or y+z==x # if you want to avoid the order of numbers issue
    # or return (x+y==z and x<y) or (x+z==y and x<z) or (y+z==x and y<z) # if you want to avoid the order of numbers issue and to check if x is smaller than other two numbers
    # or return (x+y==z and x<y) or (x+z==y and x<z) or (y+z==x and y<z) # if you want to avoid the order of numbers issue and to check if x is smaller than other two numbers
    # or return (x+y==z and x<y) or (x+z==y and x<z) or (y+z==x and y<z) # if you want to avoid the order of numbers issue and to check if x is smaller than other two numbers
    # or return (x+y==z and x<y) or (x+z==y and x<z) or (y+z==x and y<z) # if you want to avoid the order of numbers issue and to check if x is smaller than other two numbers
    # or return (x+y==z and x<y) or (x+z==y and x<z) or (y+z==x and y<z) # if you want to avoid the order of numbers issue and to check if x is smaller than other two numbers
    # or return (x+y==z and x<y) or (x+z==y and x<z) or (y+z==x and y<z) # if you want to avoid the order of numbers issue and to check if x is smaller than other two numbers
    # or return (x+y==z and x<y) or (x+z==y and x<z) or (y+z==x and y<z) # if you want to avoid the order of numbers issue and to check if x is smaller than other two numbers
    # or return (x+y