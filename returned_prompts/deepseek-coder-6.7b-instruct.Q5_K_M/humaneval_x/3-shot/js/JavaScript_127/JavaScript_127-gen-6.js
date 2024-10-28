  // get the max start and min end
  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);

  // calculate length of intersection
  let length = end - start + 1;

  // if the length is less than 2, then it doesn't intersect or it is just a point
  if (length < 2) {
    return "NO";
  }

  // check if the length is a prime number
  for (let i = 2, sqrt = Math.sqrt(length); i <= sqrt; i++) {
    if (length % i == 0) {
      return "NO";
    }
  }
  return "YES";
}



