  let directions = [[-1, 0], [0, -1], [1, 0], [0, 1]];
  let n = grid.length;
  let path = Array(k).fill(Infinity);
  let visited = Array(n).fill(0).map(() => Array(n).fill(false));

  const dfs = (x, y, k, p) => {
    if (k === path.length) {
      path = [...p];
      return;
    }

    for (let i = 0; i < 4; i++) {
      let nx = x + directions[i][0], ny = y + directions[i][1];
      if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
        visited[nx][ny] = true;
        dfs(nx, ny, k + 1, [...p, grid[nx][ny]]);
        visited[nx][ny] = false;
      }
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      visited[i][j] = true;
      dfs(i, j, 1, [grid[i][j]]);
      visited[i][j] = false;
    }
  }

  return path;
}
```

## 1.1.6. 

```javascript
/*
  Given a string s, return the number of substrings of s that are palindromes.
  A string is considered a palindrome if it is equal to its reverse.
  Example:
    For s = "abc", the output should be 3.
    These are ["a", "b", "c"]
    For s = "aaa", the output should be 6.
    These are ["a", "a", "a", "aa", "a", "aaa"]
  */
const countPalindromes = (s) => {
  let count = 0;
  const isPalindrome = (