def multiply_elements(t):
    result = ()
    for i in range(len(t)):
        if i < len(t) - 1:
            result += (t[i] * t[i+1],)
        else:
            result += (t[i],)
    return result