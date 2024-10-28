    vowels = 'aeiouAEIOU'
    return ''.join([c for c in text if c not in vowels])  # or use filter() and join() functions
    # or use regular expression: import re; return re.sub('[aeiouAEIOU]', '', text)
    # or use list comprehension: return ''.join([c for c in text if c.lower() not in vowels])  # or use filter() and join() functions
    # or use a loop: result = ''; for c in text: if c not in vowels: result += c; return result


