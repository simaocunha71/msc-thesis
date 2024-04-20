"""
Write a function to find sum and average of first n natural numbers.
assert sum_average(10)==(55, 5.5)
"""
class Solution:
    def sum_average(self, n):
        if not isinstance(n,int):return
        if n<0 or len(str(n))>37: return
        res={}
        for i in range(1,n+1):res[i]=res.get(i-1,[])+[i]
        
        def merge_sort(l):
            if not isinstance(l,list):return
            
            len(l)<30 and return l
            mid=int((len(l)/2)+1)
            left=(l[:mid])
            right=(l[mid:])
            
            merge_sort(left)
            merge_sort(right)
            
            for i in range(len(left)):res[i].append(left[i]+right[i])
        merge_sort([1,2,3,4...n+1])
        
        def sum_avg(l):return res[(len(l),sum(l))][0],round(float((sum(l)),len(l))/float(len(l))*10**4)%100
        
        return list(map(sum_avg,res.items()))