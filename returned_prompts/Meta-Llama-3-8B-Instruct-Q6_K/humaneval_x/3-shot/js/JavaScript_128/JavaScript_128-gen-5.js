  if (arr.length == 0) {
    return null;
  }

  let sign_product = 1;
  let sum_of_magnitudes = 0;

  for (const num of arr) {
    if (num > 0) {
      sign_product *= 1;
      sum_of_magnitudes += num;
    } else if (num < 0) {
      sign_product *= -1;
      sum_of_magnitudes += Math.abs(num);
    } else {
      sign_product *= 0;
    }
  }

  return sign_product * sum_of_magnitudes;
}  // This code should be indented properly. It seems like there is an indentation issue in the code.  // This code should be indented properly. It seems like there is an indentation issue in the code.