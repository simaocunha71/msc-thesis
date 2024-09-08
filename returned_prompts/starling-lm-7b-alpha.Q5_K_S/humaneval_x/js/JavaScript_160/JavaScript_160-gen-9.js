  let result = operand[0];
  let length = operator.length;

  for (let i = 0; i < length; i++) {
    if (operator[i] === '+') {
      result += operand[i + 1];
    } else if (operator[i] === '-') {
      result -= operand[i + 1];
    } else if (operator[i] === '*') {
      result *= operand[i + 1];
    } else if (operator[i] === '//') {
      result = Math.floor(result / operand[i + 1]);
    } else if (operator[i] === '**') {
      result = Math.pow(result, operand[i + 1]);
    }
  }

  return result;
}



