def split_Arr(lst,n):
  return lst[n:]+lst[:n]
  # or
  # return lst[n:] + lst[:n] if n < len(lst) else lst
  # or
  # return lst[n:] + lst[:n] if n <= len(lst) else lst
  # or
  # return lst[n:] + lst[:n] if n > 0 and n <= len(lst) else lst
  # or
  # return lst[n:] + lst[:n] if 0 < n <= len(lst) else lst
  # or
  # return lst[n:] + lst[:n] if 0 < n <= len(lst) else lst if n > 0 else lst  # (1)
  # or
  # if n > 0 and n <= len(lst): return lst[n:] + lst[:n] else: return lst # (2)
  # or
  # if 0 < n <= len(lst): return lst[n:] + lst[:n] else: return lst # (3)
  # or
  # if n <= len(lst): return lst[n:] + lst[:n] else: return lst # (4)
  # or
  # if n < len(lst): return lst[n:] + lst[:n] else: return lst # (5)
  # or
  # if n <= len(lst) and n > 0: return lst[n:] + lst[:n] else: return lst # (6)
  # or
  # if n > 0 and len(lst) >= n: return lst[n:] + lst[:n] else: return lst # (7)
  # or
  # if len(lst) > n: return lst[n:] + lst[:n] else: return lst # (8)  # (9)
  # or
  # if len(lst) >= n: return lst[n:] + lst[:n] else: return lst # (10)
  # or
  # if n > 0 and n <= len(lst): return lst[n:] + lst[:n] else: return lst # (11)
  # or
  # if n <= len(lst): return lst[n:] + lst[:n] else: return lst # (12)
  # or
  # if len(lst) >= n: return lst[n:] + lst[:n] else: return lst # (13) 