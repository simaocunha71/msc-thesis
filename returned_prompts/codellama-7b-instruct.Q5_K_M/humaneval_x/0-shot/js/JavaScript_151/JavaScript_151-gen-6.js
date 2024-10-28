  // doubleTheDifference([]); // 0
  // doubleTheDifference([1]); // 1
  // doubleTheDifference([1, 3, 2, 0]); // 10
  // doubleTheDifference([-1, -2, 0]); // 0
  // doubleTheDifference([9, -2]); // 81
  // doubleTheDifference([0]); // 0
  // doubleTheDifference([1, 2, 3, 4, 5]); // 55

B:
  return lst.filter(n => n >= 0 && n % 1 === 0 && n % 2 !== 0).map(n => n * n).reduce((a, b) => a + b, 0);
}