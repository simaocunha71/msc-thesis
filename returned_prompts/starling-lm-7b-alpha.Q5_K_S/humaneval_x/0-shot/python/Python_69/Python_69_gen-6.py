    def search(lst):
        if len(set(lst)) == len(lst):
            return -1
        max_num = max(lst)
        if max_num not in lst:
            return -1
        else:
            freq_dict = {}
            for i in lst:
                if i in freq_dict:
                    freq_dict[i] += 1
                else:
                    freq_dict[i] = 1
            for i in freq_dict:
                if freq_dict[i] >= i:
                    return i


B:

def search(lst):
    max_num = max(lst)
    if max_num not in lst:
        return -1
    else:
        freq_dict = {}
        for i in lst:
            freq_dict[i] = lst.count(i)
        for k in freq_dict:
            if freq_dict[k] >= k:
                return k

C:

def search(lst):
    max_num = max(lst)
    if max_num not in lst:
        return -1
    else:
        lst.sort(reverse=True)
        for i in lst:
            if i == max_num:
                lst.remove(i)
                break
        if len(lst) > max_num:
            return max_num
        else:
            return -1


```