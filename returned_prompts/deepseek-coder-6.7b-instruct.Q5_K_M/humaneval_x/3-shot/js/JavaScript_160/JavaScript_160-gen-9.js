  let result = operand[0];
  for (let i = 1; i < operand.length; i++) {
    switch (operator[i - 1]) {
      case '+':
        result += operand[i];
        break;
      case '-':
        result -= operand[i];
        break;
      case '*':
        result *= operand[i];
        break;
      case '//':
        result = Math.floor(result / operand[i]);
        break;
      case '**':
        result = Math.pow(result, operand[i]);
        break;
    }
  }
  return result;
}



