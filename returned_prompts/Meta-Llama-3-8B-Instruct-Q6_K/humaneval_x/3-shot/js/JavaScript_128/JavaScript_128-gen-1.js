  if (arr.length == 0) {
    return null;
  }
  let sign_product = 1;
  let sum_of_magnitudes = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
      sign_product *= -1;
    }
    sum_of_magnitudes += Math.abs(arr[i]);
  }
  return sign_product * sum_of_magnitudes;
}