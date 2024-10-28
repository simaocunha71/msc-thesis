  let result = [];
  for (let i = 0; i < numbers.length; i++) {
    result.push(numbers[i]);
    if (i < numbers.length - 1) {
      result.push(delimeter);
    }
  }
  return result;
};

console.log(intersperse([], 4)); // []
console.log(intersperse([1, 2, 3], 4)); // [1, 4, 2, 4, 3]
```

## 2. 프로그래밍 언어로 해보기

- JavaScript
- Python
- Java
- C#

## 3. 강의 내용

- 제어 구조
- 반복문
- 배열
- 함수
- 프로그래밍의 기본 개념
- 코드 리뷰

## 4. 학습 목표

- 프로그래밍 기본 개념을 익히고 배운다.
- 반복문, 조건문, 배열, 함수 등 기본적인 제어 구조를 이해한다.
- 프로그래밍 언어를 처음 접하는 사람들