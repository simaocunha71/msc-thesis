/*You are given two intervals,
  where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
  The given intervals are closed which means that the interval (start, end)
  includes both start and end.
  For each given interval, it is assumed that its start is less or equal its end.
  Your task is to determine whether the length of intersection of these two 
  intervals is a prime number.
  Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
  which its length is 1, which not a prime number.
  If the length of the intersection is a prime number, return "YES",
  otherwise, return "NO".
  If the two intervals don't intersect, return "NO".


  [input/output] samples:
  intersection((1, 2), (2, 3)) ==> "NO"
  intersection((-1, 1), (0, 4)) ==> "NO"
  intersection((-3, -1), (-5, 5)) ==> "YES"
  */
const intersection = (interval1, interval2) => {
  let intersection;
  if (!interval1 || !interval1.includes(interval1[0]) || !interval2 || !interval2.includes(interval2[0])) {
    return false;
  } else if (interval1[1] > interval1[0] && interval2[1] < interval2[0]) {
    // the second and third condition will be added after you pass this problem!
    intersection = true;
  } else if (!interval1[1] && !interval2) {
    return false;
  } else {
    for (let i = 1; i <= interval1[1]; i++) {
      const start = i + interval1[0];
      if ((start >= interval1[0]) && (start < interval1[1])) {
        intersection = true;
        break;
      } else if (!start) continue;
    }
  }
  return intersection ? 'YES' : 'NO';
};
