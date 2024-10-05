  const set1 = new Set(l1);
  const set2 = new Set(l2);
  return [...new Set(Array.from(set1).filter(x => set2.has(x)))]
    .sort((a, b) => a - b);
}



