  if (arr.length == 0) {
    return null;
  }

  let product = 1;
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      product *= 1;
      sum += arr[i];
    } else if (arr[i] < 0) {
      product *= -1;
      sum += arr[i];
    } else {
      product *= 0;
    }
  }

  return sum * product;
}



