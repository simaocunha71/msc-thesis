  let eaten = number + need;
  let left = remaining - (eaten - remaining);
  return [eaten, Math.max(0, left)];
}

// Example usage:
console.log(eat(5, 6, 10)); // Output: [11, 4]
console.log(eat(4, 8, 9)); // Output: [12, 1]
console.log(eat(1, 10, 10)); // Output: [11, 0]
console.log(eat(2, 11, 5)); // Output: [7, 0]
console.log(eat(0, 1000, 0)); // Output: [1000, 0]
console.log(eat(1000, 0, 0)); // Output: [1000, 0]
console.log(eat(500, 500, 0)); // Output: [1000, 0]
console.log(eat(1000, 0, 1000)); // Output: [1000, 0]
console.log(eat(1000, 1000, 1000)); // Output: [2000, 0]
console.log(eat(1000, 0, 1001)); // Output: [1001, 0]
console.log(eat(1000, 1, 1001)); // Output: [1001, 0]
console.log(eat(1000, 1001, 1001)); // Output: [2001, 0]
console.log(eat(1000, 0, 0)); // Output: [1000, 0]
console.log(eat(1000, 1000, 0)); // Output: [1000, 0]
console.log(eat(1000, 0, 1000)); // Output: [1000, 0]
console.log(eat(1000, 1000, 1000)); // Output: [2000, 0]
console.log(eat(1000, 0, 1001)); // Output: [1001, 0]
console.log(eat(1000, 1, 1001)); // Output: [1001, 0]
console.log(eat(1000, 1001, 1001)); // Output: [2001, 0]
console.log(eat(0, 0, 0