def second_smallest(nums):
    m1 = m2 = float('inf')
    for x in nums:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2