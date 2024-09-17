def extract_string(strings: list,n: int) -> list:
  extracted_strings = [s for s in strings if len(s) == n]
  return extracted_strings