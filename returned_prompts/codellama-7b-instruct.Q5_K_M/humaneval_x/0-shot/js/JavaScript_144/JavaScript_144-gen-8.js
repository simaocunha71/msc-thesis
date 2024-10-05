const simplify = (x, n) => {
  let xNum = parseInt(x.split("/")[0], 10);
  let xDen = parseInt(x.split("/")[1], 10);
  let nNum = parseInt(n.split("/")[0], 10);
  let nDen = parseInt(n.split("/")[1], 10);
  if (xDen === nDen) {
    if (xNum * nNum % xDen === 0) return true;
    return false;
  } else {
    let gcd = findGcd(xDen, nDen);
    if (xDen % gcd === 0 && nDen % gcd === 0) {
      if (xNum * nNum % xDen / gcd === 0) return true;
      return false;
    }
    return false;
  }
};

const findGcd = (a, b) => {
  if (b === 0) return a;
  else return findGcd(b, a % b);
};

console.log(simplify("1/5", "5/1"));
console.log(simplify("1/6", "2/1"));
console.log(simplify("7/10", "10/2"));

