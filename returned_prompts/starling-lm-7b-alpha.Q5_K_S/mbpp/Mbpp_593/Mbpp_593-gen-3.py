"""
def removezero_ip(ip):
    ip = ip.split(".")
    ip = [str(i) for i in ip if i != "0"]
    return ".".join(ip)
"""

def removezero_ip(ip):
    ip = ip.split(".")
    while "0" in ip:
        ip.remove("0")
    return ".".join(ip)


if __name__ == "__main__":
    print(removezero_ip("216.08.094.196"))


# Made By Mostafa_Khaled
```