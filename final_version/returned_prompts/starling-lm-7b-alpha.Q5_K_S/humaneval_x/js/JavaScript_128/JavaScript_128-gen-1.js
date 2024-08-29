  if (arr.length === 0) {
    return null;
  }

  let sign = 1;
  let result = 0;

  for (let i = 0; i < arr.length; i++) {
    sign *= arr[i] > 0 ? 1 : -1;
    result += Math.abs(arr[i]);
  }

  return result * sign;
}



