def removezero_ip(ip):
  return tuple(int(x) for x in ip.split('.') if x)  # split the string by '.' and filter out empty strings