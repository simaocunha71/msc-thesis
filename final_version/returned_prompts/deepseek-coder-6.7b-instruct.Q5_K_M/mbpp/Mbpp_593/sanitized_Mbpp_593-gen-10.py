def removezero_ip(ip_address):
    ip_parts = ip_address.split('.')
    new_ip_parts = [str(int(part)) for part in ip_parts]
    new_ip_address = '.'.join(new_ip_parts)
    return new_ip_address