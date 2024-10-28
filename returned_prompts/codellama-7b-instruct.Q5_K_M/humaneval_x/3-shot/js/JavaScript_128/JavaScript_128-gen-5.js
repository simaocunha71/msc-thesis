  if (arr.length == 0) {
    return null;
  } else {
    var product = 1;
    var sum = 0;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] > 0) {
        product *= 1;
        sum += arr[i];
      } else if (arr[i] < 0) {
        product *= -1;
        sum -= arr[i];
      } else {
        product *= 0;
        sum += 0;
      }
    }
    return product * sum;
  }
}



