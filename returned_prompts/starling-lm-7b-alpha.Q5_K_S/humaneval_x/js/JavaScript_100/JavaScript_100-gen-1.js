  const result = [];
  let stones = n;
  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) {
      result.push(stones += 2);
    } else {
      result.push(stones += 1);
    }
  }
  return result;
}



