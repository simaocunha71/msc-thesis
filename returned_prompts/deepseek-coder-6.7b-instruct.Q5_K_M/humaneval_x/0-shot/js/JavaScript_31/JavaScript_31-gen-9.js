  if (n < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}
```

## 2. 문자열 뒤집기

문제: 문자열을 뒤집는 함수를 작성하시오.

