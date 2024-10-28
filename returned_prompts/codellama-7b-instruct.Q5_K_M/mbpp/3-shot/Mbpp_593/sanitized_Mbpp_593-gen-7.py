def removezero_ip(ip):
  parts = ip.split('.')
  parts = [part.lstrip('0') for part in parts]
  parts = [part or '0' for part in parts]
  return '.'.join(parts)