  if (operator.length != operand.length - 1)
    throw new Error('Invalid input');

  var result = operand[0];
  for (var i = 1; i < operand.length; i++) {
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
        result **= operand[i];
        break;
      default:
        throw new Error('Invalid input');
    }
  }
  return result;
}



