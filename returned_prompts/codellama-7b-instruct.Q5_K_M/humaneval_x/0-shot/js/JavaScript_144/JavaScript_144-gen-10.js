const simplify = (x, n) => {
  const numX = parseInt(x.split('/')[0]);
  const numN = parseInt(n.split('/')[0]);
  const denom = parseInt(x.split('/')[1]);
  const denomN = parseInt(n.split('/')[1]);
  if (numX * denomN === numN * denom) return true;
  return false;
}
