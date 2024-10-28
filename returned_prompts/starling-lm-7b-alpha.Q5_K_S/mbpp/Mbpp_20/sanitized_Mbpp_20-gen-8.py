def is_woodall(num):
    num_str = str(num)
    return (num_str[0] != '1') and (all(num_str[i+1] == '0' or (int(num_str[i])+int(num_str[i+1])) % 3 == int(num_str[i+2]) for i in range(len(num_str)-1)))