
function intersection(a, b) {
  let start = Math.max(a[0], b[0]);
  let end = Math.min(a[1], b[1]);
  if (start <= end) {
    return [start, end];
  }
  return [];
}

const isPrime = (num) => {
  if (num < 2) {
    return false;
  }
  for (let i = 2; i < num; i += 1) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
};

const isPrimeLength = (interval) => {
  const length = interval[1] - interval[0] + 1;
  return isPrime(length);
};

const checkIsPrimeInterval = (interval) => {
  if (interval.length === 0) {
    return false;
  }
  return isPrimeLength(interval);
};

const checkIsNotPrimeInterval = (interval) => {
  if (interval.length === 0) {
    return true;
  }
  return !isPrimeLength(interval);
};

const checkIntervals = (interval1, interval2) => {
  const interval = intersection(interval1, interval2);
  if (interval.length === 0) {
    return 'NO';
  }
  return checkIsPrimeInterval(interval) ? 'YES' : 'NO';
};

module.exports = checkIntervals;

















































































































































