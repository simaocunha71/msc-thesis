  if (lst.length < 2) {
    return null;
  }
  let first = lst[0];
  let second = lst[1];
  for (let i = 2; i < lst.length; i++) {
    if (lst[i] < second) {
      second = lst[i];
    }
  }
  return second;
}



