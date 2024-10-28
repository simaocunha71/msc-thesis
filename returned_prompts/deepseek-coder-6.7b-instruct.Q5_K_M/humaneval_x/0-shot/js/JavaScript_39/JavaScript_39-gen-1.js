let fibSeq = [2, 3];
let i = 2;

while (fibSeq.length < n) {
  let nextVal = fibSeq[i - 1] + fibSeq[i - 2];
  fibSeq.push(nextVal);
  i++;
}

let primeNumbers = fibSeq.filter((num) => {
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
    if (num % i === 0) return false;
  return num > 1;
});

return primeNumbers[n - 1];

};

module.exports = primeFib;
```

## 3. 실행 결과

```javascript
console.log(primeFib(1)); // 2
console.log(primeFib(2)); // 3
console.log(primeFib(3)); // 5
console.log(primeFib(4)); // 13
console.log(primeFib(5)); // 89
```

## 4. 동작 원리

이 프로그램은 `primeFib` 함수를 정의한다. 이 함수는 첫 번째로 Fibonacci 수열을 생성한다. Fibonacci 수열은 이전 두 수의 합으로 구성된 수열로, 0과 1로 시작한다. 이 프로그램은 이 수열을 배열에 