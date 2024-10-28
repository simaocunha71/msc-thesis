  let result = [];
  for (let i = Math.min(a, b); i <= Math.max(a, b); i++) {
    if (i % 2 == 0) {
      result.push(i);
    }
  }
  return result;
}