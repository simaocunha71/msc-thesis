def removezero_ip(ip):
    ip = ip.split(".")
    while "0" in ip:
        ip.remove("0")
    return ".".join(ip)