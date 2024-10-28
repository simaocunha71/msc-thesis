    def is_substring(s1, s2):
        for i in range(len(s1)):
            if s1[i:i+len(s2)] == s2:
                return True
        return False

    return is_substring(a, b) or is_substring(a, b[::-1]) or is_substring(a, b[1:]) or is_substring(a, b[:-1]) or is_substring(a, b[1:-1]) or is_substring(a, b[::-1][1:]) or is_substring(a, b[::-1][:-1]) or is_substring(a, b[1:-1][::-1]) or is_substring(a, b[1:-1][::-1][1:]) or is_substring(a, b[1:-1][::-1][:-1]) or is_substring(a, b[1:-1][::-1][1:-1]) or is_substring(a, b[1:-1][::-1][1:-1][::-1]) or is_substring(a, b[1:-1][::-1][1:-1][::-1][1:]) or is_substring(a, b[1:-1][::-1][1:-1][::-1][1:-1]) or is_substring(a, b[1:-1][::-1][1:-1][::-1][1:-1][::-1]) or is_substring(a, b[1:-1][::-1][1:-1][::-1][1:-1][::-1][1:]) or is_substring(a, b[1:-1][::-1][1:-1][::-1][1:-1][::-1][1:-1]) or is_substring(a, b[1:-1][::-1][1:-1][::-1][1:-1][::-1][1:-1][::-1]) or is_substring(a, b[1:-1][::-1][1:-1][::-1][1:-1][::-1][1:-1][::-1][1:]) or is_substring(a, b[1:-1][::-1][1:-1][::-1][1:-1][::-1][1:-1][::-1][1:-1]) or is_substring(a, b[1:-1][::-1][1:-1][::-1][1:-1][::-1][1:-1][::-1][1:-1][::-1]) or is_sub