  if (a > b) {
    [a, b] = [b, a];
  }

  const result = [];
  for (let i = a; i <= b; i++) {
    if (i % 2 === 0) {
      result.push(i);
    }
  }
  return result;
}