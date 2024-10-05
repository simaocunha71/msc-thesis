  // Determine the intersection of the two intervals
  const start = Math.max(interval1[0], interval2[0]);
  const end = Math.min(interval1[1], interval2[1]);

  // If the intervals don't intersect, return "NO"
  if (start > end) {
    return "NO";
  }

  // Compute the length of the intersection
  const length = end - start + 1;

  // Check if the length is a prime number
  if (length < 2) {
    return "NO";
  }
  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) {
      return "NO";
    }
  }
  return "YES";
};
*/






// Solution
function intersection(interval1, interval2) {
  // Determine the intersection of the two intervals
  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);

  // If the intervals don't intersect, return "NO"
  if (start > end) {
    return "NO";
  }

  // Compute the length of the intersection
  let length = end - start + 1;

  // Check if the length is a prime number
  if (length < 2) {
    return "NO";
  }
  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) {
      return "NO";
    }
  }
  return "YES";
}


// Example usage:
console.log(intersection([1, 2], [2, 3])); // Outputs: "NO"
console.log(intersection([-1, 1], [0, 4])); // Outputs: "NO"
console.log(intersection([-3, -1], [-5, 5])); // Outputs: "YES"


























