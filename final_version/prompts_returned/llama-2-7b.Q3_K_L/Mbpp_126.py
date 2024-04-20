"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""
class Solution:
    def __init__(self):
        self.sum = []
        
    def find(self, n1, n2):
        temp = [1] # common divisors of (1,n1), (1,n2), ...
        i = 0
        while i<len(temp):
            if len(self.sum) == 4:
                break
            
            j = i+1
            while j<len(temp) and temp[j]>1:
                self.sum += [n1%temp[i], n2%temp[i]]
                i+=1
                if temp[i]+1 == 0:
                    print("Error")
                    break
                j+=1
            i+=1
        return sum(self.sum)
        