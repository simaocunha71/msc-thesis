import re
import re
import re
def remove_lowercase(string):
    string = [x for x in string if x.isupper()]
    return ''.join(string)