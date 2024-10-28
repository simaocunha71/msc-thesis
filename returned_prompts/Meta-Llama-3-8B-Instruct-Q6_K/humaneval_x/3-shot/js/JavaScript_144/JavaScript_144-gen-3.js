  let xNum = parseInt(x.split('/')[0]);
  let xDen = parseInt(x.split('/')[1]);
  let nNum = parseInt(n.split('/')[0]);
  let nDen = parseInt(n.split('/')[1]);

  let newXNum = xNum * nDen;
  let newXDen = xDen * nNum;

  let gcd = function(a, b) {
    if (b === 0) return a;
    return gcd(b, a % b);
  };

  let g = gcd(newXNum, newXDen);
  newXNum /= g;
  newXDen /= g;

  return newXNum === newXDen;
}