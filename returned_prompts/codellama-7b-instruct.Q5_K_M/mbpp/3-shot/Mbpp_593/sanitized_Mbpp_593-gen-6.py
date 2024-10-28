def removezero_ip(ip_address: str) -> str:
  return '.'.join(str(int(x)) for x in ip_address.split('.') if int(x) != 0)