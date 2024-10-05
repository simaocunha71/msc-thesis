  let result = [];
  for(let i = 1; i <= n; i++) {
    if(i % 2 === 0) {
      result.push(factorial(i));
    } else {
      result.push(sum(i));
    }
  }
  return result;
}

const factorial = (number) => {
  let result = 1;
  for(let i = 2; i <= number; i++) {
    result *= i;
  }
  return result;
}

const sum = (number) => {
  let result = 0;
  for(let i = 1; i <= number; i++) {
    result += i;
  }
  return result;
}



