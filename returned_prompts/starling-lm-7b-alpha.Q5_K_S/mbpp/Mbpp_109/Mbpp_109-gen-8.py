def odd_Equivalent(s,n):
    cnt = 0
    for i in range(n):
        for j in range(len(s)):
            if int(s[j]) % 2 == 1:
                cnt += 1
        s = s[-1]+s[:-1]
    return cnt

assert odd_Equivalent("011001",6) == 3

# 解析：
# 主要是找到旋转后的串中的奇数，因为每次旋转时，奇数的位置是固定的。
# 首先，我们遍历旋转n次的字符串中的每个位置，如果这个位置的值是奇数，那么我们就加1。
# 然后我们通过将最后一个字符加到开头，来实现旋转。
# 这样我们就可