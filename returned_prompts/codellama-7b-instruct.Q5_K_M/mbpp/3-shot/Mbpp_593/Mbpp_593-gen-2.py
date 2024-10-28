
def removezero_ip(ip: str) -> str:
  return '.'.join(str(int(x)).rstrip('0') for x in ip.split('.'))


