
    def search(lst):
        m = {}
        for i in lst:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        max_num = max(m.keys())
        max_frequency = m[max_num]
        for num in m.keys():
            if m[num] >= num and max_frequency < m[num]:
                return num
        return -1























# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #























def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''

    def get_frequency(lst, num):
        count = 0
        for i in lst:
            if i == num:
                count += 1
        return count

    m = {}
    for i in lst:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1

    max_num = max(m.keys())
    max_frequency = m[max_num]
    for num in m.keys():
        if get_frequency(lst