
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum += lst[i]
    return sum

print(solution([5, 8, 7, 1])) #==> 12
print(solution([3, 3, 3, 3, 3])) #==> 9
print(solution([30, 13, 24, 321])) #==>0
print(solution([3, 4, 5, 6, 7, 8])) #==> 15
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #==> 15


This function works by iterating over the list, and for each element at an even index, it checks whether that element is odd. If it is, it adds it to the sum. The result is the sum of all odd numbers at even indices.
<jupyter_output>
<empty_output>
<jupyter_text>
