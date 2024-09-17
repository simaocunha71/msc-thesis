def removezero_ip(ip: str) -> str:
  return '.'.join(str(int(num)) for num in ip.split('.'))