  let count = 0;
  
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "(") {
      count++;
    } else if (brackets[i] === ")") {
      count--;
      if (count < 0) {
        return false;
      }
    }
  }
  
  return count === 0;
};

console.log(correctBracketing("(")); // false
console.log(correctBracketing("()")); // true
console.log(correctBracketing("(()())")); // true
console.log(correctBracketing(")(()")); // false


// 정답: 주어진 문자열에 괄호의 쌍이 맞는지 확인하는 함수이다.
// 괄호의 쌍이 잘 맞으려면 각각의 여는 괄호에는 닫는 괄호가 있어야 하며, 닫는 괄호의 개수는 여는 괄호의 개수보다 적거나 같아야 한다.
// 따라서 나의 함수는 여는 괄호의 개수와 닫는 괄호의 개수를 각각