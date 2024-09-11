def removezero_ip(ip):
  return '.'.join(str(int(x)) for x in ip.split('.') if x)  # or use re.sub(r'^0+\.?','.',ip) for a more concise solution