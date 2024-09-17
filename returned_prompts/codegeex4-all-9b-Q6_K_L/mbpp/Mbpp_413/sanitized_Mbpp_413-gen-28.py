def extract_nth_element(tuples: list,n: int) -> list:
  return [tuple[i] for tuple in tuples for i in range(len(tuple)) if i == n]