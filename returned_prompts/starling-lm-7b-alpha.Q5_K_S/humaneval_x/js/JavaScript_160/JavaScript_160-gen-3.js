  let result = operand[0];
  for (let i = 1; i < operand.length; i++) {
    let operator_i = operator[i - 1];
    let operand_i = operand[i];
    if (operator_i == '+') {
      result += operand_i;
    } else if (operator_i == '-') {
      result -= operand_i;
    } else if (operator_i == '*') {
      result *= operand_i;
    } else if (operator_i == '//') {
      result //= operand_i;
    } else if (operator_i == '**') {
      result = Math.pow(result, operand_i);
    }
  }
  return result;
}



