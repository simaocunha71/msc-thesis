
def round_and_sum(nums):
    sum = 0
    for num in nums:
        sum += round(num)
    return sum * len(nums)

print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))
<jupyter_output>
243.0
<jupyter_text>
Question 5:
<jupyter_code>
