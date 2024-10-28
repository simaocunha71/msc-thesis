  var sum = 0;
  var i = 0;

  while (i < k) {
    var num = arr[i];
    if (num < 10) {
      sum += num;
    } else if (num < 100) {
      sum += num % 10;
    }
    i += 1;
  }

  return sum;
}