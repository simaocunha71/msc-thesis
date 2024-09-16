"""
def text_lowercase_underscore(text):
    return all(c.islower() for c in text) and all('_' in text for i in range(len(text)-1))
"""