
def removezero_ip(ip_address):
    while '0.' in ip_address:
        ip_address = ip_address.replace('0.','.',1)
    return ip_address


