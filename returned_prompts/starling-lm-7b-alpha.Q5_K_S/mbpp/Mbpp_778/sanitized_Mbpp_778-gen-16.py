def pack_consecutive_duplicates(lst):
    packs = []
    current_pack = []
    for i in lst:
        if current_pack or i != lst[0]:
            current_pack.append(i)
        else:
            packs.append(current_pack)
            current_pack = [i]
    packs.append(current_pack)
    return packs