def removezero_ip(ip):
  return '.'.join(str(int(x)) for x in ip.split('.') if x)  # removing leading zero and splitting the ip address