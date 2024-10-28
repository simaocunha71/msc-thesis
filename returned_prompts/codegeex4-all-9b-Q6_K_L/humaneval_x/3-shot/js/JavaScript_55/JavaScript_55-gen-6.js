  let fibNums = [1, 1];

  for (let i = 2; i < n; i++) {
    fibNums.push(fibNums[i - 1] + fibNums[i - 2]);
  }

  return fibNums[n - 1];
}



