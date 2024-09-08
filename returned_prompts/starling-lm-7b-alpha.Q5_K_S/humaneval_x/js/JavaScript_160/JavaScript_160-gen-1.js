  const ops = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '//': (a, b) => Math.floor(a / b),
    '**': (a, b) => Math.pow(a, b)
  }

  function do_algebra(operands, operators) {
    if (operators.length == 1) {
      return operands[operators[0]];
    }
    const left = do_algebra(operands, operators.slice(0, -1));
    const op = operators[operators.length - 1];
    const right = do_algebra(operands, operators.slice(0, -1));
    return ops[op](left, right);
  }

  return do_algebra(operand, operator);
}



