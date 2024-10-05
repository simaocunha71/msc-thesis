
  let start1 = interval1[0];
  let end1 = interval1[1];
  let start2 = interval2[0];
  let end2 = interval2[1];

  let intersectStart, intersectEnd;

  if (start1 <= start2 && end1 >= start2 && end1 <= end2) {
    intersectStart = start1;
    intersectEnd = start2;
  } else if (start2 <= start1 && end2 >= start1 && end2 <= end1) {
    intersectStart = start2;
    intersectEnd = start1;
  } else {
    return "NO";
  }

  return isPrime(intersectEnd - intersectStart) ? "YES" : "NO";
};

const isPrime = num => {
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
};
