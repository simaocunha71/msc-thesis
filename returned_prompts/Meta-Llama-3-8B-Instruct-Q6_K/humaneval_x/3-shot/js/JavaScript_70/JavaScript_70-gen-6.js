  if (!lst.length) return [];
  const sorted = lst.slice().sort((a, b) => a - b);
  const result = [];
  while (sorted.length > 0) {
    result.push(sorted.shift());
    if (sorted.length > 0) {
      result.push(sorted.pop());
    }
  }
  return result;
}