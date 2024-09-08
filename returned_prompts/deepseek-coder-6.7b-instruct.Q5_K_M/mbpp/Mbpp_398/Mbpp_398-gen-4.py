def sum_of_digits(lst):
    sum_list = []
    for i in lst:
        sum = 0
        for j in str(i):
            sum += int(j)
        sum_list.append(sum)
    return sum_list

print(sum_of_digits([10,2,56]))

#Output: [1, 2, 11]

#Explanation: 
#The sum of the digits of 10 is 1, the sum of the digits of 2 is 2, and the sum of the digits of 56 is 11.
#So, the function returns the list [1, 2, 11].
<jupyter_output>
[1, 2, 11]
<jupyter_text>
