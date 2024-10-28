const simplify = (x, n) => {
  const [a, b] = x.split('/');
  const [c, d] = n.split('/');
  return (Number(a) * Number(d)) % Number(b) === 0;
};

