
def change_date_format(date):
    return date[8:]+'-'+date[5:7]+'-'+date[:4]

print(change_date_format("2026-01-02"))

"""
Explanation:
This solution uses string slicing to extract and rearrange the date parts. 
The key is to use the indices of the string correctly.
"""
<jupyter_output>
02-01-2026
<jupyter_text>
Example 3
<jupyter_code>
