  let set1 = new Set(l1);
  let set2 = new Set(l2);
  let commonSet = new Set([...set1].filter(x => set2.has(x)));
  return Array.from(commonSet).sort((a, b) => a - b);
}