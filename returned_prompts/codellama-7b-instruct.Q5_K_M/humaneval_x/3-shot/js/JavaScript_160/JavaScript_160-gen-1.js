  let result = operand[0];
  for (let i = 0; i < operator.length; i++) {
    switch (operator[i]) {
      case '+':
        result += operand[i+1];
        break;
      case '-':
        result -= operand[i+1];
        break;
      case '*':
        result *= operand[i+1];
        break;
      case '//':
        result = Math.floor(result / operand[i+1]);
        break;
      case '**':
        result = result ** operand[i+1];
        break;
    }
  }
  return result;
}



