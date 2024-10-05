  return l.map((v, i) => i % 3 === 0 ? l.slice(i).sort()[0] : v);
}