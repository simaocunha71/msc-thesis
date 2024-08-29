  let result = [3];

  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(1 + i / 2);
    } else {
      result.push(result[result.length - 1] + result[result.length - 2] + result[result.length - 3]);
    }
  }

  return result;
}



