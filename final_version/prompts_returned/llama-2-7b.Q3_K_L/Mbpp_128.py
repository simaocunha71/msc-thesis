"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""
# Time Limit Exceeded
class Solution:
    def longWords(self, n, dictionary):
        """
        :type dictionary: List[str]
        :param dictionary: A list of words (without repetition)
        :param n: An integer
        :return: A list of strings that are longer than n characters.
        """
        
        count = collections.Counter(dictionary).most_common(n+1)
        return [word for word,count in count]
