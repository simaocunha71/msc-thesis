  var sum = 0;

  for (let i = 0; i < k; i++) {
    var num = arr[i];
    while (num >= 10) {
      num = num % 10;
    }
    sum += num;
  }

  return sum;
}