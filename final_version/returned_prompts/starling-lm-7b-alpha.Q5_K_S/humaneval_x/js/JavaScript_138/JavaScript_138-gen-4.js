  for (let i = 0; i <= n; i++) {
    for (let j = 0; j <= n; j++) {
      for (let k = 0; k <= n; k++) {
        for (let l = 0; l <= n; l++) {
          if (i + j + k + l === n && i % 2 === 0 && j % 2 === 0 && k % 2 === 0 && l % 2 === 0) {
            return true;
          }
        }
      }
    }
  }
  return false;
}



