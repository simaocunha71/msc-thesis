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


print(odd_Equivalent("011001",6))


"""
时间复杂度：O(n)
空间复杂度：O(1)
"""









"""
注意到s的每一个位置都会在旋转后对应到一个不同的位置，因此我们可以将s看作是一个循环列表，每次旋转都是对循环列表左移一位，即：s = s[1:]+s[0]。

那么我们可以通过将s左移n次得到的字符串中的奇数位的数字的数量来得到答案。

我们可以通过遍历s，统计奇数位的数字的数量来得到答案。

在遍历s的时候，我们需要将每个字符转换为整型，然后对其取模，以确定其是否为奇数。

最后，我们需要返回奇数位的数字的数量。
"""


"""
思路：

1. 对s进行扩展，使其长度为2n。
2. 遍历扩展后的s，将所有的数字转换为整型。
3. 对所有的数字取模，以确定其是否为奇数。
4.