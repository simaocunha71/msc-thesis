  if (arr.length == 0) {
    return null;
  }

  let sign_product = 1;
  let magnitude_sum = 0;

  for (const n of arr) {
    if (n == 0) {
      magnitude_sum = 0;
    } else if (n > 0) {
      magnitude_sum += n;
    } else {
      magnitude_sum -= n;
    }
    sign_product *= n != 0 ? n / Math.abs(n) : 1;
  }

  return magnitude_sum * sign_product;
}



