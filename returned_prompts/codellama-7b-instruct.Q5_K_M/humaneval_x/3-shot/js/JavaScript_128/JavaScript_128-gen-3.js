  if (arr.length == 0) {
    return null;
  }

  let product = 1;
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    let current = arr[i];
    if (current > 0) {
      product *= 1;
      sum += current;
    } else if (current < 0) {
      product *= -1;
      sum += current;
    } else if (current == 0) {
      product *= 0;
      sum += current;
    }
  }

  return sum * product;
}



