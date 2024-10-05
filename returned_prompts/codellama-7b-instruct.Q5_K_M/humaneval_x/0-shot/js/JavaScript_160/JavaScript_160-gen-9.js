  const expression = operand.map((value, index) => {
    let result = value;
    if (index > 0) {
      const operatorValue = operator[index - 1];
      switch (operatorValue) {
        case '+':
          result += operand[index - 1];
          break;
        case '-':
          result -= operand[index - 1];
          break;
        case '*':
          result *= operand[index - 1];
          break;
        case '//':
          result = Math.floor(result / operand[index - 1]);
          break;
        case '**':
          result **= operand[index - 1];
          break;
      }
    }
    return result;
  });
  return expression[expression.length - 1];
};

const testCases = [[['+', '-', '*'], [2, 3, 4, 5]], [['+', '-', '*'], [2, 3, 4, 5, 6, 7]], [['+', '-', '*'], [2, 3, 4, 5, 6, 7, 8]]];

for (let i = 0; i < testCases.length; i++) {
  const testCase = testCases[i];
  console.log('doAlgebra', testCase, '=>', doAlgebra(testCase[0], testCase[1]));
}

































































































































































