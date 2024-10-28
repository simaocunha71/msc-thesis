def removezero_ip(ip: str) -> str:
  ip = ip.split('.')
  ip = [int(i) for i in ip]
  ip = [str(i) for i in ip]
  ip = '.'.join(ip)
  return ip