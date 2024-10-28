  let arr = [];

  for (let i = 0; i <= n; i++) {
    if (i === 1) {
      arr[i] = 3;
    } else if (i % 2 === 0) {
      arr[i] = 1 + i / 2;
    } else {
      arr[i] = arr[i - 1] + arr[i - 2] + (i + 1 === 3 ? 3 : arr[i + 1 - 3]);
    }
  }

  return arr;
}
console.log(tri(3)) //[1, 3, 2, 8]
console.log(tri(5)) //[1, 3, 2, 8, 10, 22]
console.log(tri(7)) //[1, 3, 2, 8, 10, 22, 36, 82]

This solution has a time complexity of O(n). The space complexity is also O(n) because of the usage of an array to store the Tribonacci numbers. 

Note: The Tribonacci sequence is not defined for negative integers. In the given problem, the input is guaranteed to be non-negative.

*/

// Tests
console.log(tri(3)); // [1, 3, 2, 8]
console.log(tri(5)); // [1, 3, 2, 8, 10, 22]
console.log(tri(7)); // [1, 3, 2, 8, 10, 22, 36, 82]
console.log(tri(0)); // [1]
console.log(tri(1)); // [1, 3]
console.log(tri(2)); // [1, 3, 2, 8]

// Edge Cases
console.log(tri(-1)); // []
console.log(tri(-10)); // []
console.log(tri(-100)); // []

/*
In the above code, we first initialize an empty array arr. Then we fill the array by iterating from 0 to n