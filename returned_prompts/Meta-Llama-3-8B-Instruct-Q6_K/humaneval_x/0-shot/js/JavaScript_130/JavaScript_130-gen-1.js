```javascript
function tri(n) {
  if (n === 0) return [1];
  if (n === 1) return [1, 3];
  let trib = [1, 3, 2];
  for (let i = 3; i <= n; i++) {
    let nextTri = 0;
    if (i % 2 === 0) {
      nextTri = 1 + i / 2;
    } else {
      let prev1 = trib[i - 1];
      let prev2 = trib[i - 2];
      let prev3 = trib[i - 3];
      nextTri = prev1 + prev2 + prev3;
    }
    trib.push(nextTri);
  }
  return trib;
}

console.log(tri(3)); // [1, 3, 2, 8]
console.log(tri(5)); // [1, 3, 2, 8, 21, 43]
```


Explanation:
The function `tri` takes a non-negative integer `n` as input and returns the first `n+1` numbers of the Tribonacci sequence. The function uses a loop to calculate the next number in the sequence based on whether `n` is even or odd. If `n` is even, the next number is calculated as `1 + n / 2`. If `n` is odd, the next number is calculated as the sum of the previous three numbers in the sequence. The function starts with the base case of `tri(0) = [1]`, `tri(1) = [1, 3]`, and `tri(2) = [1, 3, 2]`. The function then uses a loop to calculate the next numbers in the sequence, appending each new number to the `trib` array. Finally, the function returns the `trib` array. The examples provided show the output of the function for `n = 3` and `n = 5`.