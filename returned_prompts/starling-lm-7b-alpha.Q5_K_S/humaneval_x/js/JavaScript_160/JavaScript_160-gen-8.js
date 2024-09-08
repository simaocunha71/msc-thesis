  let result = operand[0];
  for (let i = 1; i < operand.length; i++) {
    if (i % 2 == 0) {
      result = doAlgebraHelper(result, operand[i], operator[i - 1]);
    }
  }
  return result;
}

const doAlgebraHelper = (a, b, operator) => {
  let result;
  if (operator == '+') {
    result = a + b;
  } else if (operator == '-') {
    result = a - b;
  } else if (operator == '*') {
    result = a * b;
  } else if (operator == '/') {
    result = a / b;
  } else if (operator == '//') {
    result = Math.floor(a / b);
  } else if (operator == '**') {
    result = a ** b;
  }
  return result;
}



