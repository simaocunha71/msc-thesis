def move_zero(lst):
    zero_count = lst.count(0)
    new_lst = [i for i in lst if i != 0]
    new_lst.extend([0]*zero_count)
    return new_lst