  if (a + b > c && a + c > b && b + c > a) {
    let s = (a + b + c) / 2;
    return Math.round((Math.sqrt(s * (s - a) * (s - b) * (s - c))) * 100) / 100;
  } else {
    return -1;
  }
}
// Test cases:
console.log(triangleArea(3, 4, 5)); // 6.00
console.log(triangleArea(1, 2, 10)); // -1
console.log(triangleArea(2, 3, 4)); // 2.00
console.log(triangleArea(5, 6, 7)); // 9.00
console.log(triangleArea(1, 1, 2)); // -1
console.log(triangleArea(10, 10, 10)); // -1
console.log(triangleArea(1, 2, 1)); // -1
console.log(triangleArea(2, 2, 2)); // -1
console.log(triangleArea(0.5, 0.5, 1)); // -1
console.log(triangleArea(0.5, 0.5, 1.5)); // 0.50
console.log(triangleArea(1, 2, 3)); // 1.50
console.log(triangleArea(2, 3, 4)); // 2.00
console.log(triangleArea(3, 4, 5)); // 6.00
console.log(triangleArea(4, 5, 6)); // 9.00
console.log(triangleArea(5, 6, 7)); // 9.00
console.log(triangleArea(6, 7, 8)); // 12.00
console.log(triangleArea(7, 8, 9)); // 12.00
console.log(triangleArea(8, 9, 10)); // 12.00
console.log(triangleArea(9, 10, 11)); // 12.00
console.log(triangleArea(10, 11, 12)); // 12.00
console.log(triangleArea(11, 12, 13)); // 12.00
console.log(triangleArea(12