const simplify = (x, n) => {
  const numX = x.split('/')[0] * 1;
  const numN = n.split('/')[0] * 1;
  const denom = x.split('/')[1] * 1;
  if (numX * numN % denom === 0) return true;
  return false;
};
