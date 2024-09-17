def find_length(s):
    l = len(s)
    for i in range(l):
        for j in range(i+1,l+1):
            if s[i] == '0' and s[j-1] == '1':
                if j-i > len(s[i:j]):
                    len_of_string = len(s[i:j])
                else:
                    len_of_string = j-i
    return len_of_string