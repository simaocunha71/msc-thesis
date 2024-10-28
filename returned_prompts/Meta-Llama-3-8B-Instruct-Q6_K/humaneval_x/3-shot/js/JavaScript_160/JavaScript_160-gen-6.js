  let expression = operand[0];
  for (let i = 0; i < operator.length; i++) {
    expression += ` ${operator[i]} ` + operand[i + 1];
  }
  return eval(expression);
}