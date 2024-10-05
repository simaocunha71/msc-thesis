  const str = x.toString();
  const len = str.length;

  if (shift >= len) {
    return str.split('').reverse().join('');
  }

  return str.slice(shift) + str.slice(0, shift);
};

console.log(circularShift(12, 1)); // "21"
console.log(circularShift(12, 2)); // "12"
```

## 다른 사람의 풀이

```javascript
const circularShift = (x, shift) => {
  const str = String(x);
  const len = str.length;
  return str.slice(len - shift) + str.slice(0, len - shift);
};

console.log(circularShift(12, 1)); // "21"
console.log(circularShift(12, 2)); // "12"
```

이 풀이는 훨씬 간단하다. 그들은 문자열 슬라이스 메소드를 사용하여 두 부분으로 나눠서 문자열을 만들었다. 두 번째 부분은 shift만큼 오른쪽으로 이동한 부분이고, 첫 번째 부분은 나머지 부분이다. 원래 문자열의 뒷부