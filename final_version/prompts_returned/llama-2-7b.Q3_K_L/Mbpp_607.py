"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""
# @CourseraWay 2020.8
class Solution(object):
    def findMatches(self, s, p, start=0, end=-1):
        if not s:
            return [], [start], [end]
        
        for i in range(len(s)):
            # 受到字符追加后对应的索引值改变，因此需要每次遍历
            if p.search(s[i:]) == None or end == -1:
                continue
            
            start, end = i+p.start(), i + p.end()
            
            yield s[start:end], start, end
        
        # 当前字符串不是匹配的时候，则返回 [] 并且提示其他的搜索结果为空
        return [], [end]