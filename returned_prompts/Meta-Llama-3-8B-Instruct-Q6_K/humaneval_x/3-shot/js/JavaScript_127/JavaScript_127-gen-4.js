  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);
  
  if (start > end) {
    return "NO";
  }
  
  let length = end - start;
  
  let isPrime = true;
  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) {
      isPrime = false;
      break;
    }
  }
  
  return isPrime ? "YES" : "NO";
}