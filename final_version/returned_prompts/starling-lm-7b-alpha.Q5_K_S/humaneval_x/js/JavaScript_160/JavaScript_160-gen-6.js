  const do_operation = (left, right, op) => {
    switch (op) {
      case '+': return left + right;
      case '-': return left - right;
      case '*': return left * right;
      case '//': return Math.floor(left / right);
      case '**': return left ** right;
    }
  }

  const ops = [];
  const ops_to_do = [];

  for (let i = 0; i < operator.length; i++) {
    if (operator[i] == '**') {
      const left = operand[ops.length];
      const right = operand[ops.length + 1];
      ops.push(operator[i]);
      ops.push(operator[i + 1]);
      ops_to_do.push(do_operation(left, right, operator[i]));
      i += 1;
    } else {
      ops.push(operator[i]);
      ops_to_do.push(do_operation(operand[ops.length], operand[ops.length + 1], operator[i]));
    }
  }

  return ops_to_do.reduce((acc, v) => acc + v, 0);
}



