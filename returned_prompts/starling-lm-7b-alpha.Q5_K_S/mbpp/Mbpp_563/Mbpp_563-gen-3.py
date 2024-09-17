
def extract_values(s: str) -> list:
  return [elem[1:-1] for elem in s.split('", "')]


