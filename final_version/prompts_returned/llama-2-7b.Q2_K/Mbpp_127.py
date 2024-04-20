"""
Write a function to multiply two integers.
assert multiply_int(10,20)==200
"""
from typing import List
def multiply_int(num: int , numTwo: int):
    result = [0] * (20-len(str(int(num)))) + str(int(num))
    for i in range(1, 10):
        result += "0" if (int(i)*int(num) < 10) else str(int(i))
        
    for i in range(1, len(str(int(numTwo)))-2, 2):
        if int(num) > 0:
            result += f"*{str(int(numTwo)/int(num))}{str(int(numTwo))}"
        else:
            result += "*" + str(int(numTwo))
            
    for i in range(1, len(str(int(num)))):
        if int(num) > 0:
            result = "+".join([str(x) for x in [result, f"*{str(int(num)*int(int))}"]])
            
    return result[:len(str(int(num))))]
