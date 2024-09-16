def next_smallest_palindrome(n):
    n_str = str(n)
    length = len(n_str)
    if length == 1:
        return int(n_str[0]) + 1
    if length == 2:
        if n_str[0] == n_str[1]:
            return int(n_str[0] + str(int(n_str[0]) + 1))
        else:
            return int(n_str[0] + str(int(n_str[1]) + 1))
    else:
        if n_str[0] == n_str[1]:
            return int(n_str[0] + str(int(n_str[2:length]) + 1))
        else:
            return int(n_str[0] + str(int(n_str[1:length]) + 1))

next_smallest_palindrome(1000000000)
