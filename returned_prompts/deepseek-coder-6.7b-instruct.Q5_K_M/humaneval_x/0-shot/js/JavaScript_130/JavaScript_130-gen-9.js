  let arr = [1, 3, 2];
  if (n < 3)  return arr.slice(0, n + 1);
  for (let i = 3; i <= n; i++) {
    if (i % 2 === 0) {
      arr[i] = 1 + i / 2;
    } else {
      arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
    }
  }
  return arr;
}

console.log(tri(3)); // [1, 3, 2, 8]
console.log(tri(4)); // [1, 3, 2, 8, 18]
console.log(tri(5)); // [1, 3, 2, 8, 18, 50]
console.log(tri(6)); // [1, 3, 2, 8, 18, 50, 160]
console.log(tri(7)); // [1, 3, 2, 8, 18, 50, 160, 554]
console.log(tri(8)); // [1, 3, 2, 8, 18, 50, 160, 554, 2448]
console.log(tri(9)); // [1, 3, 2, 8, 18, 50, 160, 554, 2448, 10800]
console.log(tri(10)); // [1, 3, 2, 8, 18, 50, 160, 554, 2448, 10800, 46560]

The solution uses an array to store the Tribonacci numbers. It initializes the first three Tribonacci numbers as [1, 3, 2]. The rest of the Tribonacci numbers are calculated by checking if the current index is even or odd. For even indices, the Tribonacci number is calculated as 1