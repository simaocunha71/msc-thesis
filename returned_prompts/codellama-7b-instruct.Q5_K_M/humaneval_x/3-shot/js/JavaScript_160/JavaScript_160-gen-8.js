  let result = operand[0];
  for (let i = 0; i < operator.length; i++) {
    const op = operator[i];
    const opd = operand[i + 1];
    switch (op) {
      case '+':
        result += opd;
        break;
      case '-':
        result -= opd;
        break;
      case '*':
        result *= opd;
        break;
      case '//':
        result = Math.floor(result / opd);
        break;
      case '**':
        result = Math.pow(result, opd);
        break;
    }
  }
  return result;
}



