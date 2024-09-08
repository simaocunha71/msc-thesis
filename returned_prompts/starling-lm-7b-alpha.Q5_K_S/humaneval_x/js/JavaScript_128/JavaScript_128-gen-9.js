  if (arr.length == 0) {
    return null;
  }
  let sign = 1;
  let result = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == 0) {
      sign *= 0;
    } else if (arr[i] > 0) {
      sign *= 1;
    } else {
      sign *= -1;
    }
    result += Math.abs(arr[i]) * sign;
  }
  return result;
}



