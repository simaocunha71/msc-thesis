  let result = [1, 3];
  if (n <= 1) {
    return result.slice(0, n + 1);
  }

  for (let i = 2; i <= n; i++) {
    let next = 0;
    if (i % 2 === 0) {
      next = 1 + i / 2;
    } else {
      next = result[i - 1] + result[i - 2] + result[i - 3];
    }
    result.push(next);
  }
  return result;
}
// You can also use memoization for this problem to avoid redundant calculations
// const tri = (n) => {
//   let memo = [1, 3];
//   for (let i = 2; i <= n; i++) {
//     memo[i] = i % 2 === 0 ? 1 + i / 2 : memo[i - 1] + memo[i - 2] + memo[i - 3];
//   }
//   return memo.slice(0, n + 1);
// };
//  tri(3) = [1, 3, 2, 8]  // example result
//  tri(4) = [1, 3, 2, 8, 11]  // example result
//  tri(5) = [1, 3, 2, 8, 11, 19]  // example result
//  tri(6) = [1, 3, 2, 8, 11, 19, 33]  // example result
//  tri(7) = [1, 3, 2, 8, 11, 19, 33, 55]  // example result
//  tri(8) = [1, 3, 2, 8, 11, 19, 33, 55, 89]  // example result
//  tri(9) = [1, 3, 2, 8, 11, 19, 33, 55, 89, 144]  // example result
//  tri(10) = [1, 3, 2, 8, 11, 19, 33, 55, 89, 144, 233]  // example result
//  tri(