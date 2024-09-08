def find_Volume(base, height, length):
    # formula to find volume of a triangular prism is (base*height*length)/2
    volume = (base*height*length)/2
    return volume

print(find_Volume(10,8,6))

# Output: 240.0
assert find_Volume(10,8,6) == 240

print("All test cases pass")
<jupyter_output>
240.0
All test cases pass
<jupyter_text>
Question 2:Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.You may assume that each input would have exactly one solution, and you may not use the same element twice.Example:Given nums = [2, 7, 11, 15], target = 9,Because nums[0] + nums[1] = 2 + 7 = 9,return [0, 1].
<jupyter_code>
