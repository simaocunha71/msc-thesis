  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] > lst[i + 1]) return false;
  }
  return new Set(lst).size == lst.length;
}