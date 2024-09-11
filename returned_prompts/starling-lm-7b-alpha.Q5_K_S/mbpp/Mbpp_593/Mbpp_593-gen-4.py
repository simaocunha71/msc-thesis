"""

def removezero_ip(s):
    l = list(s.split('.'))
    for i in range(len(l)):
        while len(l[i])>1 and l[i][0]=='0':
            l[i] = l[i][1:]
    return '.'.join(l)

print(removezero_ip("216.08.094.196"))

"""

# Here are some tips:
# - The IP address is a string of four parts, separated by periods.
# - The parts can be empty, and if so, they are represented by a single period.
# - A part can be a single zero, and if so, it is represented by a single zero.
# - A part can have leading zeroes, and you are to remove those.
# - The function is expected to return the same number of parts, and they are to be separated by periods.
# - The test case is assert removezero_ip("216.08.094.196")==('216.8.94.196')

"""

def removezero_ip(s):
    parts = s.split('.')
    for i in range(len(parts)):
        if parts[i]=='':
            parts[i] = '.'
        elif parts[i][0] == '0':
            parts[i] = parts[i][1:]
    return '.'.join(parts)

print(removezero_ip("216.08.094.196"))

"""

# Here are some tips:
# - The IP address is a string of four parts, separated by periods.
# - The parts can be empty, and if so, they are represented by a single period.
# - A part can be a single zero, and if so, it is represented by a single zero.
# - A part can have leading zeroes, and you are to remove those.
# - The function is expected to return the same number of parts, and they are to be separated by periods.
# - The test case is assert removezero_ip("216.08.094.