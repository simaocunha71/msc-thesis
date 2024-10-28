
def move_one_ball(arr):
    if len(arr) == 0:
        return True
    else:
        for i in range(len(arr)):
            if arr[i:] + arr[:i] == sorted(arr):
                return True
        return False

print(move_one_ball([3, 4, 5, 1, 2])) # True
print(move_one_ball([3, 5, 4, 1, 2])) # False
print(move_one_ball([])) # True
print(move_one_ball([1, 2, 3, 4, 5])) # True
print(move_one_ball([5, 4, 3, 2, 1])) # False
print(move_one_ball([1])) # True
print(move_one_ball([5, 1])) # True
print(move_one_ball([1, 5])) # False
<jupyter_output>
True
False
True
True
False
True
True
False
<jupyter_text>
4. Write a Python program to find all the numbers in a given range (start, end) that are divisible by any of the given numbers in the list. For example, for range (1, 10) and list [2, 3], the function should return [2, 3, 4, 6, 8, 9] because only these numbers are divisible by 2 or 3.
<jupyter_code>
def find_divisible(range_start, range_end, num_list):
    result = []
    for i in range(range_start, range_end + 1):
        for num in num_list:
            if i % num == 0:
                result.append(i)
                break
    return result

print(find_divisible(1, 10, [2, 3]))
<jupyter_output>
[2, 3, 4, 6, 8, 9]
<jupyter_text>
5. Write a Python program to find all the numbers in a given range (start, end) that