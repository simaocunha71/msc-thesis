  let result = operand[0];

  for (let i = 1; i < operand.length; i++) {
    let op = operator[i - 1];
    let num1 = operand[i - 1];
    let num2 = operand[i];
    if (op == '+') {
      result += num1;
    } else if (op == '-') {
      result -= num1;
    } else if (op == '*') {
      result *= num1;
    } else if (op == '//') {
      result = Math.floor(result / num1);
    } else if (op == '**') {
      result = Math.pow(result, num1);
    }
  }

  return result;
}



