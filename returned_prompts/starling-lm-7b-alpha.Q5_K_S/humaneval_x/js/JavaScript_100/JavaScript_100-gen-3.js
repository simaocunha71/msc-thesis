  let result = [];
  let current = n;

  for (let i = 0; i < n; i++) {
    result.push(current);
    current += (i % 2 == 0) ? 2 : 1;
  }

  return result;
}



