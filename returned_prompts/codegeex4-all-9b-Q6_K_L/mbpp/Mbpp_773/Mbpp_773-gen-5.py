def occurance_substring(main_str: str, substr: str) -> tuple:
  if substr not in main_str:
    return None
  position = main_str.find(substr)
  return (substr, position, position+len(substr)-1)


