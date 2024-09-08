def divisible_by_n(lst, n):
    return [x for x in lst if x % n == 0]

print(divisible_by_n([10,20,40,50,30], 10))

#assert divisible_by_n([10,20,40,50,30], 10)==[10,20,30,40]
<jupyter_output>
[10, 20, 30, 40]
<j