from math import log
from copy import deepcopy
def odd_Equivalent(s,n):
    # 深拷贝，防止递归过程中的变量覆盖
    s = deepcopy(s)
    # 对s进行扩展
    for i in range(n):
        # 左移
        s = "".join([s[i] for i in range(1,len(s))])+s[0]

    # 统计所有奇数位的数字
    odd_count = 0
    for i in range(len(s)):
        if int(s[i]) % 2 == 1:
            odd_count += 1

    return odd_count