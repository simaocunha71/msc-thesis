def removezero_ip(ip: str) -> str:
  ip = list(ip)
  for i in range(len(ip)):
    if ip[i] != "0":
      break
    else:
      del ip[i]
  return "".join(ip)