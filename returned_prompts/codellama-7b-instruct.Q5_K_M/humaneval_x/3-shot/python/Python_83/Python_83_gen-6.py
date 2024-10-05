    return len([s for s in range(10**(n-1), 10**n) if str(s)[0] == '1' or str(s)[-1] == '1'])


