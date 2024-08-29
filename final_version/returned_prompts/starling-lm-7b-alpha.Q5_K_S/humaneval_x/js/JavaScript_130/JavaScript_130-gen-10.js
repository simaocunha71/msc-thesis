  let result = [];
  for (let i = 1; i < n + 2; i++) {
    if (i % 2 == 0) {
      result.push(3);
    } else {
      if (i == 1) {
        result.push(1);
      } else if (i == 2) {
        result.push(2);
      } else {
        result.push(result[result.length - 1] + result[result.length - 2] + result[result.length - 3]);
      }
    }
  }
  return result;
}



