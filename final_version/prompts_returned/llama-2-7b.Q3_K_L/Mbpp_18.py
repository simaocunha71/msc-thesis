"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""
class Solution:
    def removeDirtyChars(self, s1: str, s2: str) -> str:
        if not (len(set(s1)) & len(set(s2)))  # 去掉笔记中的有误字符，只剩下有误字符相同的。
            return s1  # 没有过滤出来的就直接返回原始字符串。
        set_str = "".join(sorted(set(s2)))    # 将笔记中所有识别到的误字符字母串连起来，并排序。
        return s1.replace(set_str, "", 1)   # 用字符串的replace方法去掉指定字元。replace()返回一个新的字符串。
