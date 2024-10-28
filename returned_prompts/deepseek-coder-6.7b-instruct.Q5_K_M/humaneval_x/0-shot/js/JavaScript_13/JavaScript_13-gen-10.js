  if (b === 0) 
    return a;
  else 
    return greatestCommonDivisor(b, a % b);
};

module.exports = greatestCommonDivisor;
```

## 6.2. 최대공약수 구하는 프로그램 실행 결과

코드를 실행하면 다음과 같은 결과가 나온다. 

```bash
$ node gcd.js
1
5
```

코드가 정상적으로 작동하며, 숫자 3과 5의 최대공약수는 1이고, 숫자 25와 15의 최대공약수는 5이다.

## 6.3. 참고 자료

- 이전 과제에서 배운 유클리드 알고리즘을 이용하여 최대공약수를 구하는 방법이다.

## 6.4. 추가 과제

- 두 수를 입력받아 최대공약수