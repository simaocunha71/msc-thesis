  var count = 0;

  for (var i = 0; i < arr.length; i++) {
    var num = Math.abs(arr[i]);
    var sum = 0;
    while (num > 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    if (sum > 0) {
      count++;
    }
  }

  return count;
}



