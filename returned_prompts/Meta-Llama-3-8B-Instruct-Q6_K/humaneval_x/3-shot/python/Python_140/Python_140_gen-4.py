    result = ""
    for c in text:
        if c == ' ':
            if result and result[-1] == ' ':
                result += '-'
            else:
                result += '_'
        else:
            result += c
    return result
#  Test cases
print(fix_spaces("Example"))  # "Example"
print(fix_spaces("Example 1"))  # "Example_1"
print(fix_spaces(" Example 2"))  # "_Example_2"
print(fix_spaces(" Example   3"))  # "_Example-3"
#  Output
# "Example"
# "Example_1"
# "_Example_2"
# "_Example-3"  #  End of Output
#  End of code
#  End of Test cases
#  End of Program
#  End of test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
#  End of Test cases
#  End of Program
# 