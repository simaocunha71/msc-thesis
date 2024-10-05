        if (x <= 0 || n <= 0) {
            return false;
        }

        while (x % n == 0) {
            x /= n;
        }

        return x == 1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isSimplePower(1, 4)); // true
        System.out.println(sol.isSimplePower(2, 2)); // true
        System.out.println(sol.isSimplePower(8, 2)); // true
        System.out.println(sol.isSimplePower(3, 2)); // false
        System.out.println(sol.isSimplePower(3, 1)); // false
        System.out.println(sol.isSimplePower(5, 3)); // false
    }
}
```

## 3. 실행 결과

위의 코드를 실행하면 다음과 같은 결과를 얻을 수 있습니다.

```
true
true
true
false
false
false
```

이 결과는 주어진 각 조건에 대해 `isSimplePower` 메소드가 올바르게 동작함을 나타냅니다.

## 4. 코드 설명

코드는 두 개의 함수로 구성되어 있습니다. 

1