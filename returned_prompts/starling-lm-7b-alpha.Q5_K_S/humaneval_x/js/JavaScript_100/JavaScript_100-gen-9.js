  let result = [];
  let total = 0;
  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) {
      result.push(total + 2);
    } else {
      result.push(total + 1);
    }
    total += result[result.length - 1];
  }

  return result;
}



