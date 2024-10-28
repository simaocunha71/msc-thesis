  let count = 0;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        if ((i * i - i + 1 + j * j - j + 1 + k * k - k + 1) % 3 === 0) {
          count++;
        }
      }
    }
  }
  return count;
}
// or use set to optimize the time complexity
const getMaxTriples = (n) => {
  let count = 0;
  let seen = new Set();
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      let sum = (i * i - i + 1 + j * j - j + 1) % 3;
      if (seen.has(sum)) {
        count++;
      }
      seen.add((i * i - i + 1 + j * j - j + 1) % 3);
    }
  }
  return count;
}
// or use dynamic programming to optimize the time complexity
const getMaxTriples = (n) => {
  let count = 0;
  let dp = new Array(3).fill(0);
  for (let i = 0; i < n; i++) {
    let a = (i * i - i + 1) % 3;
    dp[a]++;
    for (let j = 0; j < 3; j++) {
      count += dp[j] * dp[(j + 1) % 3];
    }
  }
  return count;
}
// or use math to optimize the time complexity
const getMaxTriples = (n) => {
  let count = 0;
  let sum = 0;
  for (let i = 0; i < n; i++) {
    sum += (i * i - i + 1) % 3;
    count += sum / 3;
  }
  return Math.floor(count);
}
// or use math to optimize the time complexity
const getMaxTriples = (n) => {
  let count = 0;
  let sum = 0;
  for (let i = 0; i < n; i++)