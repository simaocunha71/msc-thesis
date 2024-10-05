  let start = Math.min(a, b);
  let end = Math.max(a, b);

  let result = [];

  for (let i = start; i <= end; i++) {
    if (i % 2 === 0) {
      result.push(i);
    }
  }

  return result;
}



