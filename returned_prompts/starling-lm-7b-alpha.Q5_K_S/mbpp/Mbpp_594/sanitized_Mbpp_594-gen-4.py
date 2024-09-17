def diff_even_odd(list):
    l = []
    for i in range(len(list)):
        if list[i]%2==0:
            l.append(list[i])
        elif list[i]%2!=0:
            l.append(list[i])
            break
    if len(l)==2:
        return l[1]-l[0]
    else:
        return "The given list does not have an even or odd number"