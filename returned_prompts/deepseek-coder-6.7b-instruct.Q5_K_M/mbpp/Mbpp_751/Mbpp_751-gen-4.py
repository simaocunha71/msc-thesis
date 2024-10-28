
def check_min_heap(lst):
    for i in range(len(lqst)):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < len(lst) and lst[left_child] < lst[i]:
            return False
        if right_child < len(lst) and lst[right_child] < lst[i]:
            return False
    return True


