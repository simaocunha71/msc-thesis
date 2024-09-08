def count_Occurrence(tuple,list):
    count = 0
    for i in tuple:
        if i in list:
            count += 1
    return count

print(count_Occurrence(('a', 1, 'c', 2, 'd', 3),[1, 2] ))

#output: 3

#Explanation: The elements 1 and 2 are present in the tuple. So, the function returns 2.
<jupyter_output>
3
3
<jupyter_text>
