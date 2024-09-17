def removezero_ip(ip):
  ip = list(ip)
  while ip[0] == "0" and ip[1] == ".":
    ip.pop(0)
    ip.pop(0)
  return ''.join(ip)