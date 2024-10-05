  let even = l.filter((e, i) => i % 2 === 0).sort((a, b) => a - b);
  return l.map((e, i) => (i % 2 === 0) ? even.shift() : e);
}



