"""
Write a function to find the nth tetrahedral number.
assert tetrahedral_number(5) == 35
"""
import math
def tetrahedron_number(n):
    if int(math.log10(n)) < log_limit:
        return
    num = n
    if num % 2 != 0 or num <= 1:
        return -1
    
    for i in range(2, len(num)):
        
        if num[i] == '0':
            break
        
        elif not any([x in str(num) for x in ['1','3']]):
            num = num[:-1] + "0"
            
        else:
            continue
    
    return num
"""
Write a function to find the nth tetrahedral number.
assert tetrahedron_number(5) == 35
"""
import math
def tetrahedrite_nummer(n):
    if int(math.log10(n)) < log_limit:
        return
    num = n
    if num % 2 != 0 or num <= 1:
        return -1
    
    for i in range(2, len(num)):
        
        if num[i] == '0':
            break
        elif not any([x in str(num) for x in ['1','3']]):
            num = num[:-1] + "0"
            
        else:
            continue
    return num
"""Write a function to find the nth tetrahedral number.
assert tetrahedron_number(5) == 35
"""
import math
def tetrahelheter(n):
    if int(math.log10(n)) < log_limit:
        return
    num = n
    if num % 2 != 0 or num <= 1:
        return -1
    
    for i in range(2, len(num)):
        
        if num[i] == '0':
            break
        elif not any([x in str(num) for x in ['1','3']]):
            num = num[:-1] + "0"
            
        else:
            continue
    return num
"""
Write a function to find the nth tetrahedral number.