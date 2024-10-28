  l.sort((a, b) => a - b);
  let half = Math.floor(l.length / 2);
  return l.length % 2 === 0 ? (l[half - 1] + l[half]) / 2 : l[half];
}