
import re
def extract_values(s: str) -> list:
    return re.findall(r'"([^"]*)"', s)


