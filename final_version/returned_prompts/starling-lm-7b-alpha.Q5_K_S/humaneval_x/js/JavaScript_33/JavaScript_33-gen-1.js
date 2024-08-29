  const result = [...l];
  const indices = result.findIndex((_, i) => (i % 3) == 0);
  if (indices === -1) {
    return result;
  }

  const sorted = result.slice(indices).sort((a, b) => a - b);
  for (let i = indices; i < result.length; i++) {
    result[i] = sorted[i - indices];
  }

  return result;
}



