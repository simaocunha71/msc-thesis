"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""
def unique_sublists(arr):
    # Write your code here.
    out={}
    for i in arr:
        l=[]
        for el in i:
            if el in out:
                out[el]+=1
            else:
                out[el]=1
        for key,val in out.items():
            print(key)
            for k in range(0,val):
                l+=[str(k)+str(key)]
    return l

out=unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])
print(out)