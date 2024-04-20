"""
Write a python function to toggle bits of the number except the first and the last bit. 
assert toggle_middle_bits(9) == 15
"""

def toggle_middle_bits(num):
    result = 0
    
    for idx, value in enumerate(str(num)):
        # print(idx, end='\t')
        if idx % 2 == 0:
            result += int(value) * (1 - (1-int(value)))
            
            continue
        
        result = int(value) * (1 - (1-int(value)))
    return str(result)[::-1]