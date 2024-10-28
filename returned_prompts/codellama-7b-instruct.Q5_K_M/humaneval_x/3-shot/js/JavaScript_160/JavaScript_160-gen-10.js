  var result = 0;

  for (var i = 0; i < operator.length; i++) {
    switch (operator[i]) {
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



