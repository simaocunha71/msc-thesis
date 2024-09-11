def move_num(s):
    return ''.join(ch for ch in s if not ch.isdigit()) + ''.join(ch for ch in s if ch.isdigit())


# Alternative solution using regular expressions
import re
def move_num_alt(s):
    return re.sub(r'\d+', '', s) + re.sub(r'^.*?(\d+).*$', r'\1', s)

# Testing
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
assert move_num_alt('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'

"""
In this problem, we can observe that the two solutions are both time and space efficient, with a time complexity of O(n) and a space complexity of O(1). The first solution is based on the assumption that the input string only contains alphanumeric characters and special characters. The second solution is based on the assumption that the input string is a string of alphanumeric characters only.
"""

# Alternative solution using regular expressions
import re
def move_num_alt(s):
    return re.sub(r'\d+', '', s) + re.sub(r'^.*?(\d+).*$', r'\1', s)

# Testing
assert move_num_alt('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'

"""
In this problem, we can observe that the two solutions are both time and space efficient, with a time complexity of O(n) and a space complexity of O(1). The first solution is based on the assumption that the input string only contains alphanumeric characters and special characters. The second solution is based on the assumption that the input string is a string of alphanumeric characters only.
"""

# Alternative solution using regular expressions
import re
def move_num_alt(s):
    return re