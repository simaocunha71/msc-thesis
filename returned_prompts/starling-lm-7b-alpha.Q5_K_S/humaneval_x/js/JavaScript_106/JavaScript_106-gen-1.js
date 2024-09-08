  const factorial = (n) => {
    if (n == 0) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }

  let result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(factorial(i));
    } else {
      result.push(sum(1, i));
    }
  }

  return result;
}

const sum = (start, end) => {
  if (start > end) {
    return 0;
  } else {
    return end - start + 1 + sum(start + 1, end);
  }
}



