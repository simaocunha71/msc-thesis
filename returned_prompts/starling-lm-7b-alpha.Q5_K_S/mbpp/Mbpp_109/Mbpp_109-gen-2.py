
def odd_Equivalent(binary_str: str, n: int) -> int:
  binary_str = "".join([str(int(binary_str[i])^int(binary_str[(i+n)%len(binary_str)])) for i in range(len(binary_str))])
  return binary_str.count("1")


