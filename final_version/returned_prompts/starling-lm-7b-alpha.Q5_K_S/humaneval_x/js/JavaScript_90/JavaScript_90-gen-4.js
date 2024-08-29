  if (lst.length < 2) return null;

  let sorted = lst.slice().sort((a, b) => a - b);
  if (sorted[0] === sorted[1]) return null;
  return sorted[1];
}



