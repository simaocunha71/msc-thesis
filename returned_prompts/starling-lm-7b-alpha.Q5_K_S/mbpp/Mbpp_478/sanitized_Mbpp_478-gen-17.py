def remove_lowercase(s: str) -> str:
  return s.replace(str(chr(i) for i in range(97,97+26)), '')