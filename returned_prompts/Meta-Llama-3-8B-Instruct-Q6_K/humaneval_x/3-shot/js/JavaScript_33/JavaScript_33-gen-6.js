  return l.filter((x, i) => i % 3 !== 0).concat(l.filter((x, i) => i % 3 === 0).sort((a, b) => a - b));
}