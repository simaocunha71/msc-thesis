  if (!q.every((x, i) => x === q[q.length - 1 - i])) {
    return false;
  }
  return q.reduce((a, b) => a + b, 0) <= w;
}
// Test cases
console.log(willItFly([1, 2], 5)); // false
console.log(willItFly([3, 2, 3], 1)); // false
console.log(willItFly([3, 2, 3], 9)); // true
console.log(willItFly([3], 5)); // true
console.log(willItFly([1, 1, 1], 2)); // true
console.log(willItFly([1, 2, 3], 6)); // false
console.log(willItFly([4, 4], 8)); // true
console.log(willItFly([1, 1, 1, 1], 4)); // true
console.log(willItFly([1, 1, 1, 1], 3)); // false
console.log(willItFly([1, 1, 1, 1, 1], 5)); // false
console.log(willItFly([1, 1, 1, 1, 1], 6)); // true
console.log(willItFly([1, 1, 1, 1, 1, 1], 6)); // true
console.log(willItFly([1, 1, 1, 1, 1, 1], 7)); // false
console.log(willItFly([1, 1, 1, 1, 1, 1, 1], 8)); // true
console.log(willItFly([1, 1, 1, 1, 1, 1, 1], 9)); // false
console.log(willItFly([1, 1, 1, 1, 1, 1, 1, 1], 10)); // true
console.log(willItFly([1, 1, 1, 1, 1, 1, 1, 1, 1], 11)); // false
console.log(willItFly([1, 1, 1, 1, 1