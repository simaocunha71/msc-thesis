  var result = [];

  for (let i = 0; i < n; i++) {
    if (i % 2 == 0) {
      result.push(i);
    } else {
      var sum = 0;
      for (let j = 1; j <= i; j++) {
        sum += j;
      }
      result.push(sum);
    }
  }

  return result;
}



