  let set1 = new Set(l1);
  let set2 = new Set(l2);
  let intersection = new Set([...set1].filter(x => set2.has(x)));
  return Array.from(intersection).sort((a, b) => a - b);
} 



