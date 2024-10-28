  if (arr.length == 0) {
    return null;
  }

  var result = 1;
  var product = 1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == 0) {
      result = 0;
    } else if (arr[i] > 0) {
      product *= 1;
    } else {
      product *= -1;
    }
  }

  return result * product;
}



