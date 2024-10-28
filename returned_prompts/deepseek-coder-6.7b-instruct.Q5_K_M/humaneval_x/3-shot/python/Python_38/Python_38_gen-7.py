    # split string to groups. Each of length 3.
    groups = [s[(3  * i):min((3 * i + ))] for i in range((len(s) 2)  // 3)]
    # uncycle elements in each group. Unless group has fewer elements than 3.
    groups 
    return "".join(groups)


