let result = false;
let dp = Array(a.length).fill(1).reduce(() => Array(a.length).fill(false), []);

for (let i = 0; i < a.length; i++) {
  dp[i][i] = true;
}

for (let i = 0; i < a.length - 1; i++) {
  if (a[i] === a[i + 1]) {
    dp[i][i + 1] = true;
  }
}

for (let len = 3; len <= a.length; len++) {
  for (let i = 0; i < a.length; i++) {
    if (len > a.length - i) {
      break;
    }
    if (a[i] === a[len - 1]) {
      dp[i][len - 1] = dp[i + 1][len - 2];
    }
  }
}

for (let i = 0; i < a.length; i++) {
  for (let j = i; j < a.length; j++) {
    if (dp[i][j]) {