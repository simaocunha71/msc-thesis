  let [xNum, xDen] = x.split('/');
  let [nNum, nDen] = n.split('/');

  let gcd = (a, b) => {
    if (b == 0) {
      return a;
    } else {
      return gcd(b, a % b);
    }
  };

  let commonDivisor = gcd(parseInt(xNum), parseInt(nDen));
  let xNumSimplified = parseInt(xNum) / commonDivisor;
  let nDenSimplified = parseInt(nDen) / commonDivisor;

  if (xNumSimplified * parseInt(nNum) / nDenSimplified == 1) {
    return true;
  } else {
    return false;
  }
}



