  let sum = 0;
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] % 2 === 0) {
      sum += lst[i];
    }
  }
  return sum;
}  // Example: add([4, 2, 6, 7]) should return 2 (4 + 2)  // Example: add([1, 3, 5]) should return 0 (no even numbers)  // Example: add([2, 4, 6]) should return 4 (2 + 2)  // Example: add([1, 2, 3, 4, 5, 6]) should return 6 (2 + 4)  // Example: add([1, 2]) should return 2 (2)  // Example: add([1]) should return 0 (no even numbers)  // Example: add([]) should throw an error (empty list)  // Example: add([4, 2, 6, 7, 8]) should return 6 (4 + 2)  // Example: add([4, 2, 6, 7, 8, 10]) should return 8 (4 + 2 + 2)  // Example: add([4, 2, 6, 7, 8, 10, 12]) should return 10 (4 + 2 + 2 + 2)  // Example: add([1, 3, 5, 7, 9, 11]) should return 0 (no even numbers)  // Example: add([2, 4, 6, 8, 10, 12]) should return 12 (2 + 4 + 2 + 4)  // Example: add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) should return 10 (2 + 4 + 2 + 2)  // Example: add([1, 3, 5]) should return 0 (no even numbers)  // Example: add([2, 4, 6]) should return 4 (2 + 2)  // Example: add([1, 2]) should return 2 (2)  // Example: add([1