
def merge_dictionaries_three(*dicts: dict) -> dict:
  result = {}
  for d in dicts:
    result.update(d)
  return result


