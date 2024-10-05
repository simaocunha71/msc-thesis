
def find_max(words):
    return max(words, key=lambda x: len(set(x)))

# 这个方法比较简单，但是时间复杂度是O(n^2)，空间复杂度是O(n)，因为需要把字符串分别存放到set中，如果set中的元素数量超过了10000的话，就会报错，因为set的最大长度是10000。

