  var result = operand[0];

  for (var i = 0; i < operator.length; i++) {
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
        result = Math.floor(result / operand[i + 1]);
        break;
      case '**':
        result **= operand[i + 1];
        break;
    }
  }

  return result;
}



