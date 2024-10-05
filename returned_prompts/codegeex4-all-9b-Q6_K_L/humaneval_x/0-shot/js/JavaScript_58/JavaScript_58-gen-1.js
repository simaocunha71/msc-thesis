const common = (l1, l2) => {
  const set1 = new Set(l1);
  const set2 = new Set(l2);
  const commonElements = [...new Set([...set1].filter(x => set2.has(x)))];

  return commonElements.sort((a, b) => a - b);
};