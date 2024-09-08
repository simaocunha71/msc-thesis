def find_Max_Num(nums):
    str_nums = [str(i) for i in nums]
    str_nums.sort(reverse=True)
    return int(''.join(str_nums))

assert find_Max_Num([1,2,3]) == 321
assert find_Max_Num([5,4,3,2,1]) == 54321
assert find_Max_Num([9,8,7,6,5]) == 98765
assert find_Max_Num([0,0,0,0,0]) == 0
assert find_Max_Num([9,9,9,9,9]) == 99999
assert find_Max_Num([8,7,5,2,1]) == 87521
assert find_Max_Num([9,6,3,2,1]) == 96321
assert find_Max_Num([8,5,2,1]) == 8521
assert find_Max_Num([7,5,2,1]) == 7521
assert find_Max_Num([7,5,2,1,0]) == 75210
assert find_Max_Num([7,5,2,0,0]) == 75200
assert find_Max_Num([7,5,0,0,0]) == 75000
assert find_Max_Num([7,0,0,0,0]) == 70000
assert find_Max_Num([0,0,0,0,0]) == 0

print("All test cases pass")
<jupyter_output>
All test cases pass
<jupyter_text>
Problem 2
<jupyter_code>
