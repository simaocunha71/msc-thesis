
def max_val(lst):
    lst_num = [i for i in lst if type(i) == int or type(i) == float]
    return max(lst_num)

print(max_val(['Python', 3, 2, 4, 5, 'version']))
<jupyter_output>
5
<jupyter_text>
