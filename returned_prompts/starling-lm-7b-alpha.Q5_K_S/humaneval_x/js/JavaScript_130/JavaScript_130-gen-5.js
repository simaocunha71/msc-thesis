  let result = [];
  for (let i = 0; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(3);
    } else if (i === 1) {
      result.push(1);
    } else {
      result.push(result[result.length - 3] + result[result.length - 2] + result[result.length - 1]);
    }
  }

  return result;
}



