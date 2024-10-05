  let result = operand[0];

  for (let i = 0; i < operator.length; i++) {
    const operator_ = operator[i];
    const operand_ = operand[i + 1];
    switch (operator_) {
      case '+':
        result += operand_;
        break;
      case '-':
        result -= operand_;
        break;
      case '*':
        result *= operand_;
        break;
      case '//':
        result = Math.floor(result / operand_);
        break;
      case '**':
        result = Math.pow(result, operand_);
        break;
      default:
        break;
    }
  }

  return result;
}



