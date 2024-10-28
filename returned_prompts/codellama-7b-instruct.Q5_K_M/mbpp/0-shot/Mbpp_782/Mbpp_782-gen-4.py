def odd_length_sum(my_list):
    n = len(my_list)
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            ans += sum(my_list[i-1:j])
    return ans
