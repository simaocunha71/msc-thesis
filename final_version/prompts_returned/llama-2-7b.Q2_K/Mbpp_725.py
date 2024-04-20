"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""
from typing import Any, List

def extract_quotation(text: str):
    """
    :param text: str
    :return: List[str]
        A list of strings extracted between quotation marks.
    """
    words = text.split()
    
    def get_quotes(index, len1=0, len2=0):
        if index >= len(words) - 1 or (len1 == 0 and len2 != 0):
            return ''
        
        if len1 == 0:
            result = words[index][:len2]
            
        elif len2 == 0:
            result = words[index + 1][:-len1]
            
        else:
            result = words[index][:len2 - len1 :]   # len1 + len2 - index - 1
        
        if result == '' or result.find('"') != -1 and not result.strip():
            return get_quotes(index, len1=0)  # Infinite loop, go on
        
        return str(result).replace("\"","")
    
    return [' '.join([get_quotes(i, 0, 2) for i in range((len1 + len2), (len1 + len2 + 1)])) for j in range(len(words)): get_quotes(j, len1=j > 0 and j < len(words) - 1, len2=j == len(words) - 1)]
        
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']