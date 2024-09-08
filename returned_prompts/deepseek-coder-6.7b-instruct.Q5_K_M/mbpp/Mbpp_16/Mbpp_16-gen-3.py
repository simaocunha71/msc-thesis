def text_lowercase_underscore(s):
    return all(c.islower() or c == '_' for c in s)

assert text_lowercase_underscore("aab_cbbbc") == True
assert text_lowercase_underscore("aab_Cbbbc") == False
assert text_lowercase_underscore("aab_cbbbc_d") == True
assert text_lowercase_underscore("aab_cbbbc_D") == False
assert text_lowercase_underscore("aab_cbbbc_3") == False
assert text_lowercase_underscore("aab_cbbbc_") == True
assert text_lowercase_underscore("aab_cbbbc__d") == False
assert text_lowercase_underscore("_aab_cbbbc") == False
assert text_lowercase_underscore("aab_cbbbc_d_") == True
assert text_lowercase_underscore("_aab_cbbbc_d_") == False
assert text_lowercase_underscore("_aab_cbbbc_d_e") == False
"""
Test Cases:

1) "aab_cbbbc" => True
2) "aab_Cbbbc" => False
3) "aab_cbbbc_d" => True
4) "aab_cbbbc_D" => False
5) "aab_cbbbc_3" => False
6) "aab_cbbbc_" => True
7) "aab_cbbbc__d" => False
8) "_aab_cbbbc" => False
9) "aab_cbbbc_d_" => True
10) "_aab_cbbbc_d_" => False
11) "_aab_cbbbc_d_e" => False
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3:
<jupyter_code>
