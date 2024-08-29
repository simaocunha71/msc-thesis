  if (arr.length == 0) {
    return null;
  }

  let result = 0;
  let sign_product = 1;
  for (const num of arr) {
    if (num == 0) {
      sign_product *= 0;
    } else if (num > 0) {
      sign_product *= 1;
    } else {
      sign_product *= -1;
    }
    result += Math.abs(num) * sign_product;
  }

  return result;
}



