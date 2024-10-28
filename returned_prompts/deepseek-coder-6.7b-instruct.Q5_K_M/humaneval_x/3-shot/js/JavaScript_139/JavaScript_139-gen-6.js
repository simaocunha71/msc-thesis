  let result = 1;

  while(n > 0) {
    result *= factorial(n);
    n--;
  }

  return result;
}

const factorial = (n) => {
  let result = 1;

  while(n > 0) {
    result *= n;
    n--;
  }

  return result;
}



