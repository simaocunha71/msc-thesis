  let result = operand[0];
  for (let i = 0; i < operator.length; i++) {
    let op = operator[i];
    let operand1 = result;
    let operand2 = operand[i + 1];
    switch (op) {
      case '+':
        result = operand1 + operand2;
        break;
      case '-':
        result = operand1 - operand2;
        break;
      case '*':
        result = operand1 * operand2;
        break;
      case '//':
        result = Math.floor(operand1 / operand2);
        break;
      case '**':
        result = operand1 ** operand2;
        break;
    }
  }
  return result;
}
