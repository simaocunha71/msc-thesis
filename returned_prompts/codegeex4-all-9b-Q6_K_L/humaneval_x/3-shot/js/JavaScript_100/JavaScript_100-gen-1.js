  let result = [n];
  let current = n;
  let next = n;
  while (true) {
    next += 2;
    if (next >= n) {
      break;
    }
    result.push(next);
    current = next;
  }
  return result;
}