  const sorted = lst.slice().sort((a, b) => a - b);
  if (sorted.length < 2) return null;
  return sorted[1];
};



