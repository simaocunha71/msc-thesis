  let result = operand[0];

  for (let i = 1; i < operator.length; i++) {
    const operator_i = operator[i];
    const operand_i = operand[i];
    if (operator_i == '+') {
      result += operand_i;
    } else if (operator_i == '-') {
      result -= operand_i;
    } else if (operator_i == '*') {
      result *= operand_i;
    } else if (operator_i == '//') {
      result = Math.floor(result / operand_i);
    } else if (operator_i == '**') {
      result = Math.pow(result, operand_i);
    }
  }
  return result;
}



