  let result = operand[0];

  for (let i = 1; i < operator.length; i++) {
    let op = operator[i];
    let val = operand[i + 1];

    if (op == '+') {
      result += val;
    } else if (op == '-') {
      result -= val;
    } else if (op == '*') {
      result *= val;
    } else if (op == '//') {
      result = Math.floor(result / val);
    } else if (op == '**') {
      result = Math.pow(result, val);
    }
  }

  return result;
}



