def larg_nnum(lst,n):
    lst.sort(reverse=True)
    return lst[:n]

print(set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)))

#Alternative solution
def largest_n(lst, n):
    return sorted(lst, reverse=True)[:n]

print(set(largest_n([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)))

#Both of the solutions return the two largest numbers from the list in descending order.

#NOTE: The sorted function here doesn't sort the original list, instead it returns a new list that is sorted.
#Also, the set function is used to remove any possible duplicates from the list. If you want to maintain duplicates in the result, you can remove it.
<jupyter_output>
{90, 100}
{90, 100}
<jupyter_text>
**1.7**
<jupyter_code>
