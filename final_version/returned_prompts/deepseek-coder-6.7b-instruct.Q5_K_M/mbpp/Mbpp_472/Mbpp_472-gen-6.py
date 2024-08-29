
def check_Consecutive(l):
    for i in range(len(l)-1):
        if l[i] + 1 != l[i+1]:
            return False
    return True

print(check_Consecutive([1,2,3,4,5])) # True

# Alternate Solution:

def check_Consecutive_v2(l):
    return sorted(l) == list(range(min(l), max(l)+1))

print(check_Consecutive_v2([1,2,3,4,5])) # True
<jupyter_output>
True
True
<jupyter_text>
