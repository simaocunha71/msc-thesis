def removezero_ip(ip):
  return ".".join(map(str, map(int, ip.split('.'))))
  # or 
  return '.'.join(str(int(x)) for x in ip.split('.'))  # Python 3.5+