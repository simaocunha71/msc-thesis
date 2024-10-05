  const copy = l.map(x => x);
  const indices = copy.reduce((acc, val, idx) => {
    if (idx % 3 === 0) {
      acc.push(idx);
    }
    return acc;
  }, []);

  indices.forEach(i => {
    const sorted = copy.slice().sort();
    l[i] = sorted[i];
  });

  return l;
}



