def remove_lowercase(s):
  return s.upper().replace('ON', '').replace('TH', '').replace('PY', '')
  # or
  return ''.join([i for i in s if i.isupper()])
  # or
  return ''.join([i for i in s if i.isupper() or i == ' ']) # to keep spaces