  const result = operand[0];
  for (let i = 0; i < operand.length - 1; i++) {
    const currentOperator = operator[i];
    const nextOperand = operand[i + 1];
    switch (currentOperator) {
      case '+':
        result += nextOperand;
        break;
      case '-':
        result -= nextOperand;
        break;
      case '*':
        result *= nextOperand;
        break;
      case '//':
        result /= nextOperand;
        break;
      case '**':
        result **= nextOperand;
        break;
    }
  }

  return result;
}
