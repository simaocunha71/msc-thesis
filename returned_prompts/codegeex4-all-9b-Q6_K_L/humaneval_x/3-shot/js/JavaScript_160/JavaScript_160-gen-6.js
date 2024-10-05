  let result = operand[0];

  for (let i = 0; i < operator.length; i++) {
    let operation = operator[i];
    let value = operand[i + 1];

    if (operation == '+') {
      result += value;
    } else if (operation == '-') {
      result -= value;
    } else if (operation == '*') {
      result *= value;
    } else if (operation == '//') {
      result = Math.floor(result / value);
    } else if (operation == '**') {
      result = Math.pow(result, value);
    }
  }

  return result;
}



