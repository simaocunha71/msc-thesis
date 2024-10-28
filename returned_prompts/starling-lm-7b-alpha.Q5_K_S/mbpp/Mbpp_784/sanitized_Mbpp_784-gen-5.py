def mul_even_odd(l):
    ev=0
    od=0
    for i in l:
        if i%2==0:
            ev=ev*i
        else:
            od=od*i
    if od==0:
        return ev
    elif ev==0:
        return od
    else:
        return ev*od