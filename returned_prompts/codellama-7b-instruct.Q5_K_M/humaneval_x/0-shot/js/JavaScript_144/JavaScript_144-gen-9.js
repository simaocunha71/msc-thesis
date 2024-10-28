const simplify = (x, n) => {
  const xParts = x.split('/');
  const nParts = n.split('/');
  const xNum = parseInt(xParts[0]);
  const xDen = parseInt(xParts[1]);
  const nNum = parseInt(nParts[0]);
  const nDen = parseInt(nParts[1]);
  const result = xNum * nNum / xDen * nDen;
  return Number.isInteger(result);
};

