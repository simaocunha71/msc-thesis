import re
def find_adverb_position(sentence):
    pattern = r'\b(adv|ly|wise|well|fast|hard|quick|slow|loud|soft|bright|dark|far|near|up|down|in|out|on|off|through|under)\b'
    matches = re.finditer(pattern, sentence)
    for match in matches:
        return match.start(), match.end(), match.group()
    return None