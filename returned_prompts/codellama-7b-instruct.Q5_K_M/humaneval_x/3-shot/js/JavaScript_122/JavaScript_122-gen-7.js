  var sum = 0;
  for (var i = 0; i < k; i++) {
    var digit_count = arr[i].toString().length;
    if (digit_count <= 2) {
      sum += arr[i];
    }
  }

  return sum;
}



