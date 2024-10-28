  const evens = l.filter((_, i) => i % 2 === 0).sort((a, b) => a - b);
  return l.map((_, i) => (i % 2 === 0 ? evens.shift() : l[i]));
}



