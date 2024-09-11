import re
def check_str(s):
  if re.match(r'^[aeiouAEIOU]', s):
    return True
  else:
    return False
  # or return bool(re.match(r'^[aeiouAEIOU]', s)) for a one-liner solution
  # or return re.match(r'^[aeiouAEIOU]', s) is not None for a one-liner solution
  # or return s[0].lower() in 'aeiou' for a one-liner solution
  # or return any(s[0].lower() == x for x in 'aeiou') for a one-liner solution
  # or return re.search(r'^[aeiouAEIOU]', s) is not None for a one-liner solution
  # or return re.search(r'^[aeiouAEIOU]', s) for a one-liner solution
  # or return re.match(r'^[^aeiouAEIOU]', s) is None for a one-liner solution
  # or return re.match(r'^[^aeiouAEIOU]', s) for a one-liner solution
  # or return any(s[0].lower() != x for x in 'aeiou') for a one-liner solution
  # or return s[0].lower() not in 'aeiou' for a one-liner solution
  # or return not any(s[0].lower() == x for x in 'aeiou') for a one-liner solution
  # or return not s[0].lower() in 'aeiou' for a one-liner solution
  # or return s[0].lower() in 'aeiou' for a one-liner solution
  # or return re.match(r'^[aeiouAEIOU]', s) is not None for a one-liner solution
  # or return re.match(r'^[aeiouAEIOU]', s) for a one-liner solution
  # or return any(s[0].lower() == x for x in 'aeiou') for a one-liner solution
  # or return s[0].lower() in 'aeiou' for a one-liner solution
  # or return re.search(r'^[aeiouAEIOU]', s) is not None for a one-liner solution
  # or return re.search(r'^[aeiouAEIOU]', s) for a one-liner solution
  #