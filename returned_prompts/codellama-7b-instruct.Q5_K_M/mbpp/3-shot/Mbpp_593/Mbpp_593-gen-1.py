
def removezero_ip(ip_address):
  return '.'.join(str(int(i)).rjust(3,'0') for i in ip_address.split('.'))


