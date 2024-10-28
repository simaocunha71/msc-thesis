
import re

def fix_spaces(text):
    text = re.sub(" +", "-", text)
    text = text.replace(" ", "_")
    return text

