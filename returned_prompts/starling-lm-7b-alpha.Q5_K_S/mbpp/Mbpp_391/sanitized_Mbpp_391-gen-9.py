from collections import defaultdict
def convert_list_dictionary(s_list, name_list, score_list):
    d = defaultdict(dict)
    for i in range(len(s_list)):
        d[s_list[i]][name_list[i]] = score_list[i]
    return [d]