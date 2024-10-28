def replace_specialchar(s):
  res = s.replace(' ', ':')
  res = res.replace(',', ':')
  res = res.replace('.', ':')
  return res