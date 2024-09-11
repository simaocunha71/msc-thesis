def split_two_parts(lst, L):
  return (lst[:L], lst[L:]) if L <= len(lst) else (lst, [])