  let result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(fact(i));
    } else {
      result.push(sum(i));
    }
  }

  return result;
}

const fact = (n) => {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i;
  }
  return result;
}

const sum = (n) => {
  return n * (n + 1) / 2;
}



