  var result = [];
  var i = 1;

  while (i <= n) {
    if (i % 2 == 0) {
      result.push(i!);
    } else {
      var sum = 0;
      for (let j = 1; j <= i; j++) {
        sum += j;
      }
      result.push(sum);
    }
    i += 1;
  }

  return result;
}



