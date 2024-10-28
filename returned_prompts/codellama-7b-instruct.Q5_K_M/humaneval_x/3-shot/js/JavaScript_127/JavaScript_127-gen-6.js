  var result = 'NO';
  if (interval1[0] <= interval2[1] && interval1[1] >= interval2[0]) {
    var start = Math.max(interval1[0], interval2[0]);
    var end = Math.min(interval1[1], interval2[1]);
    if (start <= end) {
      if (isPrime(end - start)) {
        result = 'YES';
      }
    }
  }
  return result;
}



