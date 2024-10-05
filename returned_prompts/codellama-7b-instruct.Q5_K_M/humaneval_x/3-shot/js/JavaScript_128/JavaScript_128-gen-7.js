  if (arr.length == 0) {
    return null;
  } else {
    var sum = 0;
    var product = 1;
    for (var i = 0; i < arr.length; i++) {
      sum += Math.abs(arr[i]);
      product *= arr[i] > 0 ? 1 : arr[i] < 0 ? -1 : 0;
    }
    return product * sum;
  }
}



