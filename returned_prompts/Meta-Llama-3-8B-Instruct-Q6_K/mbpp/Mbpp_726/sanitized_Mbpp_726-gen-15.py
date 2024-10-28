def multiply_elements(t):
    result = ()
    for i in range(len(t)-1):
        result += (t[i] * t[i+1],)
    return result