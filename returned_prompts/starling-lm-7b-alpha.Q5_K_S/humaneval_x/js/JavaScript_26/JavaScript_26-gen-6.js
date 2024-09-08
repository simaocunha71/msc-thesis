  const result = [];
  const map = new Map();

  for (const n of numbers) {
    if (!map.has(n)) {
      map.set(n, true);
      result.push(n);
    }
  }

  return result;
}



