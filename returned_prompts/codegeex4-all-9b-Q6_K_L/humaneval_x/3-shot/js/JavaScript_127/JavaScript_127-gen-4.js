  let intersection = Math.min(interval1[1], interval2[1]) - Math.max(interval1[0], interval2[0]);
  if (intersection <= 0) {
    return "NO";
  } else {
    let isPrime = true;
    for (let i = 2; i <= Math.sqrt(intersection); i++) {
      if (intersection % i == 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      return "YES";
    } else {
      return "NO";
    }
  }
}