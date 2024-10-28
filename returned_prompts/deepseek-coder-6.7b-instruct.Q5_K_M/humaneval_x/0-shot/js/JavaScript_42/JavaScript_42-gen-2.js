  return l.map(x => x + 1);
};

module.exports = incrList;
```

## 테스트 코드

```javascript
const incrList = require('./incrList');

console.log(incrList([1, 2, 3])); // [2, 3, 4]
console.log(incrList([5, 3, 5, 2, 3, 3, 9, 0, 123])); // [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

## 실행 결과

```
[2, 3, 4]
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```

## 코드 설명

문제에서 요구한 대로 리스트의 각 요소를 1씩 증가시키는 함수를 만들었습니다. map 함수를 사용하여 새 배열을 반환합니다.

map 함수는 배열의 각 요소에 대해 제공된 함수를 실행하고 결과를 새 배열에 반환