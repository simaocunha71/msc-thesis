  let result = [1];
  if (n > 0) {
    result.push(3);
    if (n > 1) {
      result.push(2);
      if (n > 2) {
        for (let i = 3; i <= n; i++) {
          if (i % 2 == 0) {
            result.push(1 + i / 2);
          } else {
            let a = result[i - 1];
            let b = result[i - 2];
            let c = result[i - 3];
            result.push(a + b + c);
          }
        }
      }
    }
  }
  return result;
} 



