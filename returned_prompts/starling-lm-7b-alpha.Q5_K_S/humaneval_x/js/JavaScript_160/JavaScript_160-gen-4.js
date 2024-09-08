  let result = operand.shift();
  for (const op of operator) {
    const next_num = operand.shift();
    switch (op) {
      case '+':
        result += next_num;
        break;
      case '-':
        result -= next_num;
        break;
      case '*':
        result *= next_num;
        break;
      case '//':
        result //= next_num;
        break;
      case '**':
        result = Math.pow(result, next_num);
        break;
    }
  }

  return result;
}



