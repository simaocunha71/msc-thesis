
import re
def find_adverb_position(sentence):
    pattern = r'\b(clearly|well|good|better|best|well|surely|pretty|simply|enough|quite|fairly|seemingly|apparently|obviously|basically|initially|initially)\b'
    found = re.search(pattern,sentence)
    if found:
        return found.start(),found.end(),found[0]
    else:
        return None


