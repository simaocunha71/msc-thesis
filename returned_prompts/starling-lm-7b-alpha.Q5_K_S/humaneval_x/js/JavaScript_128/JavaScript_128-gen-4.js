  if (arr.length == 0) return null;

  let result = 0;
  let product = 1;
  for (const a of arr) {
    if (a == 0) {
      product = 0;
      break;
    } else if (a > 0) {
      product *= 1;
    } else {
      product *= -1;
    }
    result += a * product;
  }

  return result;
}



