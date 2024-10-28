def removezero_ip(ip):
    parts = ip.split('.')
    return '.'.join(part.lstrip('0') or '0' for part in parts)  # lstrip removes leading zeroes