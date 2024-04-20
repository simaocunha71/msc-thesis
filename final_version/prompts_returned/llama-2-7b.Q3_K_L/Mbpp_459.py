"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""
from typing import List, Optional

class Solution:
    def removeDuplicateLetters(self, S: str) -> str:
        """
        Do not change this function
        '''
        注意：只能修改此函数的代码，不可以修改global 变量的值。
        '''
        提示：你可以递归来实现。
        :param S:
        :return:
        """
        if len(S) <= 2: return S
        global s_count, t_count, v_count
        s_count = 0
        t_count = 0
        v_count = 0
        
        for i in range(len(S)):
            if i == len(S) -1: break
            
            c = S[i]
            j = i + 1
            while (j <= len(S)) and (c == S[j]):
                j += 1
                
            c_count, t_count, v_count = count_characters(c)
            
            if (c_count > s_count):
                s_count, t_count, v_count = v_count, t_count, c_count
        
        S1 = removeDuplicateLetters_recursive(S[:len(S)-1])
    
        return S + S1[1:]
        
    def removeDuplicateLetters_recursive(self, x: List[str]):
        global s_count, t_count, v_count
        if (len(x) <= 2):
            return [x]
            
        for i in range(len(x)):
            if i == len(x)-1: break
            
            c = x[i]
            j = i + 1
            while (j <= len(x)) and (c == x[j]):
                j += 1
                
            c_count, t_count, v_count = count_characters(c)
            
            if (c_count > s_count):
                s_count, t_count, v_count = v_count, t_count, c_count
