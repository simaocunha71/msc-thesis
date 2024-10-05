  const evenIdxElements = l.filter((_, idx) => idx % 2 === 0).sort((a, b) => a - b);
  return l.map((_, idx) => (idx % 2 === 0 ? evenIdxElements.shift() : l[idx]));
}



