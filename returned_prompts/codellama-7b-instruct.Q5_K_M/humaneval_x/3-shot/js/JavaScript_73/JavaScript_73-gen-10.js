  var min = Number.POSITIVE_INFINITY;
  var sum = 0;

  for (var i = 0; i < arr.length; i++) {
    sum += arr[i];
  }

  for (var i = 0; i < arr.length; i++) {
    sum -= arr[i];
    min = Math.min(min, Math.abs(sum));
    sum += arr[i];
  }

  return min;
}



