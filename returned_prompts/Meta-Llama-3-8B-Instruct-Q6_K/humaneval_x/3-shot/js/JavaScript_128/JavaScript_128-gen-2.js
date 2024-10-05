  if (arr.length === 0) {
    return null;
  }

  let product = 1;
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      product *= 1;
    } else if (arr[i] < 0) {
      product *= -1;
    }
    sum += Math.abs(arr[i]);
  }

  return product * sum;
}