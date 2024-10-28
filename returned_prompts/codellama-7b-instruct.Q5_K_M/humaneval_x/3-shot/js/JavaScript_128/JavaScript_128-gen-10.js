  if (arr.length === 0) {
    return null;
  }

  let result = 1;
  let product = 1;

  for (let i = 0; i < arr.length; i++) {
    const element = arr[i];
    if (element > 0) {
      product *= 1;
    } else if (element < 0) {
      product *= -1;
    } else {
      product *= 0;
    }

    result += Math.abs(element) * product;
  }

  return result;
}



