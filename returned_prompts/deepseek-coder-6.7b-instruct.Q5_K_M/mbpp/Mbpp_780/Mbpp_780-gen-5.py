
def longest_substring(s: str) -> str:
  seen = {}
  longest=[0,1]
  start = 0
  for i, character in enumerate(s):
    if character in seen and start <= seen[character]:
      start = seen[character]+1
    else:
      if i+1-start > longest[1]-longest[0]:
        longest = [start, i+1]
    seen[character] = i
  return s[longest[0]: longest[1]]

