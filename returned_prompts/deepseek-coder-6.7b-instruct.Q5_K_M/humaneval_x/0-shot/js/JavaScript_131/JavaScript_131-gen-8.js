  const digits = Array.from(String(n), Number);
  const odd = digits.filter(digit => digit % 2);
  return odd.length ? odd.reduce((a, b) => a * b) : 0;
}

module.exports = digits;


```

## 3. 코드 설명

입력으로 제공된 수에 대한 배열을 생성합니다. 그런 다음, 이 배열에서 홀수인 숫자를 필터링하고 그 결과를 반환합니다. 만약 홀수인 숫자가 없다면 0을 반환합니다.

## 4. 테스트 케이스

```javascript
console.log(digits(1));  // 1
console.log(digits(4));  // 0
console.log(digits(235)); // 15
console.log(digits(97531)); // 255
console.log(digits(85963)); // 1175
console.log(digits(1234567890)); // 0
```

## 5. 입력 요구사항

입력은 양의 정수여야 합니다.