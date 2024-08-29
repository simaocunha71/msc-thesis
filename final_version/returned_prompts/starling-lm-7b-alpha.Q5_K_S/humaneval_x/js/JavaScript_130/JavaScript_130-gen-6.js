  if (n === 0) return [0];
  if (n === 1) return [1];
  if (n === 2) return [1, 3];

  const result = [3];
  const tri_cache = [1, 3];

  while (result.length < n + 1) {
    if (result.length % 2 === 0) {
      result.push(tri_cache[0] + 1);
      tri_cache.shift();
    } else {
      result.push(result[result.length - 1] + result[result.length - 2] + result[result.length - 3]);
    }
  }
  return result;
};



