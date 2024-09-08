  if (lst.length < 2) {
    return null;
  }
  let smallest = Infinity;
  let second = Infinity;
  for (const n of lst) {
    if (n < smallest) {
      second = smallest;
      smallest = n;
    } else if (n < second && n != smallest) {
      second = n;
    }
  }
  return second;
}



