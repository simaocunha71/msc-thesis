def removezero_ip(ip):
  return '.'.join(str(x) for x in map(int, ip.split('.')) if x != 0)