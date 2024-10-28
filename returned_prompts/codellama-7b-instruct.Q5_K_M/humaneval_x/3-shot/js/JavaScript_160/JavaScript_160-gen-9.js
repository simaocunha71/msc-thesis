  var result = operand[0];
  var len = operand.length;
  for (let i = 0; i < len - 1; i++) {
    switch (operator[i]) {
      case '+':
        result += operand[i + 1];
        break;
      case '-':
        result -= operand[i + 1];
        break;
      case '*':
        result *= operand[i + 1];
        break;
      case '//':
        result /= operand[i + 1];
        break;
      case '**':
        result **= operand[i + 1];
        break;
    }
  }
  return result;
}



