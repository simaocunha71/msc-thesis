
def removezero_ip(ip):
    return ".".join(map(lambda x: str(int(x)), ip.split(".")))


