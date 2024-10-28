  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);
  if (start > end) {
    return "NO";
  }
  let intersection_length = end - start;
  let is_prime = true;
  for (let i = 2; i * i <= intersection_length; i++) {
    if (intersection_length % i === 0) {
      is_prime = false;
      break;
    }
  }
  return is_prime ? "YES" : "NO";
}
// Test cases
console.log(intersection([1, 2], [2, 3]));  // "NO"
console.log(intersection([-1, 1], [0, 4])); // "NO"
console.log(intersection([-3, -1], [-5, 5])); // "YES"