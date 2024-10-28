  return x.toString(base);
}
changeBase(8, 3);
changeBase(8, 2);
changeBase(7, 2);

*/


// Testing with Jest
const changeBase = require('./changeBase');

test('Convert 8 to base 3', () => {
  expect(changeBase(8, 3)).toBe('22');
});

test('Convert 8 to base 2', () => {
  expect(changeBase(8, 2)).toBe('1000');
});

test('Convert 7 to base 2', () => {
  expect(changeBase(7, 2)).toBe('111');
});

```

## 3. 정규식(Regular Expressions) 사용

정규식은 문자열을 검색하거나 추출하는 데 사용되는 패턴이다.

```javascript
// JavaScript의 정규식

const str = 'Hello, my name is John Doe';
const regex = /\bJohn Doe\b/g;  // 이름이 John Doe인 경우 찾기
const found = str.match(regex);

console.log(found);  // ['John Doe']
```

## 4. 프로그래밍 패턴

프로그래밍에서 패턴은 어떤 작업이나 조작이 반복적으로 일어나는 것을 나