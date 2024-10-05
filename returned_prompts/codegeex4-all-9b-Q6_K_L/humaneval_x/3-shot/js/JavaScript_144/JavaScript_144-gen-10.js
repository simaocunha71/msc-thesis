  let xNumerator = Number(x.split('/')[0]);
  let xDenominator = Number(x.split('/')[1]);
  let nNumerator = Number(n.split('/')[0]);
  let nDenominator = Number(n.split('/')[1]);

  if ((xNumerator * nDenominator) % (xDenominator * nNumerator) == 0) {
    return true;
  } else {
    return false;
  }
}