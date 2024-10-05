  var count = 0;
  for (let i = 0; i < arr.length; i++) {
    var sum = 0;
    var num = Math.abs(arr[i]);
    while (num > 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    if (sum > 0) {
      count += 1;
    }
  }
  return count;
}



