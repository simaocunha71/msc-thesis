
def removezero_ip(ip_address: str) -> str:
  return '.'.join(str(int(i)).zfill(3) for i in ip_address.split('.'))


