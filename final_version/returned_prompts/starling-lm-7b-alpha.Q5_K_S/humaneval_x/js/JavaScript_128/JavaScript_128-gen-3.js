  if (arr.length == 0) {
    return null;
  }

  let sign_product = 1;
  let magnitude_sum = 0;
  for (const x of arr) {
    if (x < 0) {
      sign_product *= -1;
    } else if (x > 0) {
      sign_product *= 1;
    } else {
      sign_product *= 0;
    }
    magnitude_sum += Math.abs(x);
  }
  return sign_product * magnitude_sum;
}



