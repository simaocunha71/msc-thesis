import re
def check_str(input_str: str) -> bool:
  vowel_regex = re.compile(r"^[aeiouAEIOU]")
  return vowel_regex.match(input_str)