  const copy = l.map(x => x);
  const indices = copy.reduce((acc, val, idx) => {
    if (idx % 3 === 0) acc.push(idx);
    return acc;
  }, []);
  indices.sort((a, b) => copy[a] - copy[b]);

  for (const idx of indices) {
    const val = l[idx];
    for (let i = 0; i < l.length; i++) {
      if (l[i] === val) {
        l[i] = copy[idx];
        break;
      }
    }
  }

  return l;
}



