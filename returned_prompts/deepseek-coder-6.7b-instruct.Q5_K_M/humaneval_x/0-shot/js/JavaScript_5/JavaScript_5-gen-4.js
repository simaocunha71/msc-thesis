  return numbers.reduce((accum, current, index) => {
    return index === 0 ? [...accum, current] : [...accum, delimeter, current];
  }, [])
}

console.log(intersperse([], 4)) // []
console.log(intersperse([1, 2, 3], 4)) // [1, 4, 2, 4, 3]


```

## 3. 나머지 문제

### 문제 1

다음의 JavaScript 코드를 완성하세요. 주어진 숫자 리스트에서 홀수만 리턴하는 함수를 만드세요.

```javascript
// 