  if (lst.length < 2) {
    return null;
  }
  let sorted = lst.sort((a, b) => a - b);
  if (sorted[1] === sorted[0]) {
    return null;
  }
  return sorted[1];
}



