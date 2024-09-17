def removezero_ip(ip: str) -> str:
  return '.'.join(str(int(x)) for x in ip.split('.'))

