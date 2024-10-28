
def extract_singly(lst):
  result = [i for sub in lst for i in (sub if isinstance(sub, tuple) else (sub,))]
  return result


