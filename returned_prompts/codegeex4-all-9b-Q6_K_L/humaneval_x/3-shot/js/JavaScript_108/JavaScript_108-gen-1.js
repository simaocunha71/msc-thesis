  var count = 0;
  for (const num of arr) {
    var sum = 0;
    var n = Math.abs(num);
    while (n != 0) {
      sum += n % 10;
      n = Math.floor(n / 10);
    }
    if (sum != 0) {
      count += 1;
    }
  }
  return count;
}