  var result = operand[0];
  for (let i = 1; i < operand.length; i++) {
    if (operator[i - 1] == '+') {
      result += operand[i];
    } else if (operator[i - 1] == '*') {
      result *= operand[i];
    } else if (operator[i - 1] == '-') {
      result -= operand[i];
    } else if (operator[i - 1] == '//') {
      result = Math.floor(result / operand[i]);
    } else if (operator[i - 1] == '**') {
      result = Math.pow(result, operand[i]);
    }
  }
  return result;
}