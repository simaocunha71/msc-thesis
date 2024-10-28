const simplify = (x, n) => {
  const xNum = +x.split('/')[0];
  const xDen = +x.split('/')[1];
  const nNum = +n.split('/')[0];
  const nDen = +n.split('/')[1];
  return xNum * nNum === xDen * nDen && xDen * nDen === Math.gcd(xDen, nDen);
}
