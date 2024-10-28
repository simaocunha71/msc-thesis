  let result = [];
  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) {
      let factorial = 1;
      for (let j = 1; j <= i; j++) {
        factorial *= j;
      }