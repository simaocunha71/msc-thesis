  if (a + b > c && a + c > b && b + c > a) {
    let s = (a + b + c) / 2;
    return Math.round((Math.sqrt(s * (s - a) * (s - b) * (s - c))) * 100) / 100;
  } else {
    return -1;
  }
}
// Example usage:
console.log(triangleArea(3, 4, 5)); // Output: 6.00
console.log(triangleArea(1, 2, 10)); // Output: -1
// Explanation: The given sides (1, 2, 10) do not form a valid triangle because the sum of any two sides is not greater than the third side. The function correctly returns -1 in this case.