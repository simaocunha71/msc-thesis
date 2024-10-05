  let numerator1 = parseInt(x.split("/")[0]);
  let denominator1 = parseInt(x.split("/")[1]);
  let numerator2 = parseInt(n.split("/")[0]);
  let denominator2 = parseInt(n.split("/")[1]);

  let result = numerator1 * numerator2 / denominator1 * denominator2;

  if (result % 1 == 0) {
    return true;
  } else {
    return false;
  }
}

