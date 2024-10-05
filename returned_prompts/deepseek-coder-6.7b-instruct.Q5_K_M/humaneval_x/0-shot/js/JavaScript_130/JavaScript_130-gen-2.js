  let arr = [3, 2, 8];
  if (n <= 2) return arr.slice(0, n + 1);
  let tri = [3, 2, 8];
  for (let i = 3; i <= n; i++) {
    if (i % 2 === 0) {
      tri.push(1 + i / 2);
    } else {
      tri.push(tri[i - 1] + tri[i - 2] + tri[i + 1]);
    }
  }
  return tri;
}

console.log(tri(3));
console.log(tri(5));
console.log(tri(10));
/*tri(3) should return [1, 3, 2, 8]
  tri(5) should return [1, 3, 2, 8, 14, 26]
  tri(10) should return [1, 3, 2, 8, 14, 26, 52, 98, 186, 352, 704]
  */

  // The idea here is to keep track of the last 3 numbers and use them to compute the next one. 
  // If n is even, we compute it as 1 + n / 2. If n is odd, we compute it as the sum of the last 3 numbers.




















































































































































































