
def second_largest(nums):
    m1 = m2 = float('-inf')
    for x in nums:
        if x > m1:
            m2 = m1
            m1 = x
        elif x > m2 and x != m1:
            m2 = x
    return m2


