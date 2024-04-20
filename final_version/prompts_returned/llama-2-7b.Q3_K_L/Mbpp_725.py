"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""
import re

def extract_quotation(str):
    """https://www.hackerrank.com/challenges/extract-values-from-quotes
    Explanation:
    	Input: Cortex "A53" Based "multi" tasking "Processor"
        Output: ['A53', 'multi', 'Processor']
    """
    m = re.search("[\"](.*?)[\"].*[\"](.*?)[\"].*[\"](.*?)"",str) # Regex to extract values between quotes
    return [ x.strip() for x in m.groups() ] if m else []
