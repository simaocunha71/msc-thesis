  const result = l1.filter(value => l2.includes(value));
  return [...new Set(result)].sort((a, b) => a - b);
}



