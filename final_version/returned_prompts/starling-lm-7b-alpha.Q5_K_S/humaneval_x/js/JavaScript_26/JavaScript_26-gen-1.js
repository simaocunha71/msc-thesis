  const seen = new Set();
  const result = [];

  for (const n of numbers) {
    if (!seen.has(n)) {
      seen.add(n);
      result.push(n);
    }
  }

  return result;
}



