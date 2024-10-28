const sortThird = (l) => {
  const l1 = l.map((x, i) => (i % 3 === 0) ? x : x);
  const l2 = l.map((x, i) => (i % 3 !== 0) ? x : x);
  l2.sort();
  return l1.concat(l2);
}
