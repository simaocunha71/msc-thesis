def removezero_ip(ip: str) -> str:
  return '.'.join(str(int(i)) for i in ip.split('.'))