
    sum = 0
    for i in range(1,len(lst),2):
        if lst[i]%2 == 0:
            sum += lst[i]
    return sum

print(add([4, 2, 6, 7]))

#output: 2

#Explanation:
#The even numbers at odd indices are 4(at index 1) and 6(at index 2).
#Their sum is 2.
<jupyter_output>
2
<jupyter_text>
Question 2
<jupyter_code>
