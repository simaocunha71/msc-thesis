"""
Write a function to interleave 3 lists of the same length into a single flat list.
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""
class Solution:
    def interleave(self, A: List[int], B: List[int], C: List[int]) -> List[int]:
        length_A=len(A)
        length_B=len(B)
        result=[0] * len(A)
        
        for i in range(length_A):
            if i<length_B:
                result[i]=result[i]+A[i]+int(i/length_A*length_B)+C[i%length_A]
            else:
                result[i]=result[i]+A[i]+C[i]
        
        return result