  return l.filter((x, i) => i % 2 != 0).concat(l.filter((x, i) => i % 2 == 0).sort((a, b) => a - b));
}