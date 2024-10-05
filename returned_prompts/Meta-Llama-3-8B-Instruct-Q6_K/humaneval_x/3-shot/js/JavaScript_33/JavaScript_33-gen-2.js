  return l.map((x, i) => i % 3 === 0 ? l.slice(i).sort()[0] : x);
}