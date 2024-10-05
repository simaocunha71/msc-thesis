  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
        if(num % i === 0) return false;
    return num > 1;
  }

  const intersection = (interval1, interval2) => {
    let start = Math.max(interval1[0], interval2[0]);
    let end = Math.min(interval1[1], interval2[1]);
    if (start > end) return "NO";
    return isPrime(end - start + 1) ? "YES" : "NO";
  }


