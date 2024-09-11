"""
def odd_Equivalent(s,n):
    s_odd = 0
    for i in range(len(s)):
        if s[i]=='1':
            s_odd += 1
    s_odd = s_odd%2
    if s_odd == 1:
        return 1
    else:
        return 0
    for i in range(n):
        s = ''.join(reversed(s))
        if odd_Equivalent(s,n) == 1:
            s_odd += 1
    return s_odd"""


def odd_Equivalent(s, n):
    s_odd = 0
    for i in range(len(s)):
        if s[i] == '1':
            s_odd += 1
    s_odd = s_odd % 2
    if s_odd == 1:
        return 1
    else:
        return 0
    for i in range(n):
        s = ''.join(reversed(s))
        if odd_Equivalent(s, n) == 1:
            s_odd += 1
    return s_odd


assert odd_Equivalent("011001", 6) == 3

# 作者：笨蛋
# 链接：https://www.zhihu.com/question/49956318
# 来源：知乎

# 以下是我的解答

# 首先我们需要对字符串进行翻转，翻转后的字符串中，初始字符串中的偶数位的字符对应翻转后的偶数位，奇数位的字符对应翻转后的奇数位。
# 我们可以发现，如果翻转次数是偶数，那么翻转后的字符串与原字符串是相同的，如果翻转次数是奇数，那么翻转后的字符串与原字符串是相反的。
# 我们可以发现，如果