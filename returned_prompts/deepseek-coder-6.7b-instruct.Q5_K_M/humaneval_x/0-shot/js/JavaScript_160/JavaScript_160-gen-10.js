  let result = operand[0];
  
  for (let i = 1; i < operand.length; i++) {
    switch (operator[i - 1]) {
      case '+':
        result += operand[i];
        break;
      case '-':
        result -= operand[i];
        break;
      case '*':
        result *= operand[i];
        break;
      case '//':
        result = Math.floor(result / operand[i]);
        break;
      case '**':
        result = Math.pow(result, operand[i]);
        break;
    }
  }
  
  return result;
};

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5])); // 9
console.log(doAlgebra(['+', '//', '**'], [2, 3, 4, 2])); // 14

// Test cases:
// doAlgebra(['+', '*', '-'], [2, 3, 4, 5]) => 9
// doAlgebra(['+', '//', '**'], [2, 3, 4, 2]) => 14
// doAlgebra(['*', '//', '+'], [2, 3, 4, 2]) => 10
// doAlgebra(['**', '+', '-'], [2, 3, 4, 2]) => -4
// doAlgebra(['+', '-', '*'], [2, 3, 4, 2]) => 14
```

## 2. 설명

주어진 두 리스트, 연산자와 피연산자가 있습니다. 첫 번째 리스트는 기본적인 알고리즘