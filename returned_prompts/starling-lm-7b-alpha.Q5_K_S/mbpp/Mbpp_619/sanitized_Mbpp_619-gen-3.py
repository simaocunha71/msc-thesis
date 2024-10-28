import re
import re
import re
def move_num(s):
    return ''.join(ch for ch in s if not ch.isdigit()) + ''.join(ch for ch in s if ch.isdigit())