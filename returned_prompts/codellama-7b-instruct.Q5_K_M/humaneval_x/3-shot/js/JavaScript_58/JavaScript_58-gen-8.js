  const s1 = new Set(l1);
  const s2 = new Set(l2);
  const intersection = [];

  for (let x of s1) {
    if (s2.has(x)) {
      intersection.push(x);
    }
  }

  return intersection.sort();
}



