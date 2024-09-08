  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);
  if (start <= end) {
    return [start, end];
  } else {
    return [];
  }
}

const isPrime = (length) => {
  if (length < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(length); i++) {
    if (length % i == 0) {
      return false;
    }
  }
  return true;
}



