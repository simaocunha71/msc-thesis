  let result = [];
  const sorted = arr.sort((a, b) => b - a);
  for (let i = 0; i < k; i++) {
    result.push(sorted[i]);
  }
  return result;
};



