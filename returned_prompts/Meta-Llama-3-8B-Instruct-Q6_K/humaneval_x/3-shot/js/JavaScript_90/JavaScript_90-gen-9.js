  if (lst.length < 2) {
    return null;
  }
  lst.sort((a, b) => a - b);
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] > lst[0]) {
      return lst[i];
    }
  }
  return null;
}