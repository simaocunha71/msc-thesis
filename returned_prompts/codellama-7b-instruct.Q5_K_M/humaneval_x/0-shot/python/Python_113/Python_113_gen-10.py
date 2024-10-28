
def odd_count(lst):
    output = []
    for s in lst:
        c = 0
        for i in s:
            if int(i) % 2 == 1:
                c += 1
        output.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(c, len(s), s, len(lst)))
    return output
