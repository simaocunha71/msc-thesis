def round_and_sum(lst):
    rounded_lst = [round(num) for num in lst]
    return sum(rounded_lst) * len(lst)

print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))
<jupyter_output>
243
<jupyter_text>
Question 3
<jupyter_code>
