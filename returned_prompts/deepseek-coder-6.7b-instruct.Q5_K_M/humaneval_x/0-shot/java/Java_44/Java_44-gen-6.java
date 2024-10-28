        if(x==0){
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        while(x > 0){
            sb.insert(0, x % base);
            x /= base;
        }
        return sb.toString();
    }
}

```

## 정답

문제에서 요구하는 내용을 순서대로 구현하면 되는 간단한 문제이다.

1. 입력값이 0인 경우 바로 "0"을 반환한다.
2. 입력값 x를 base로 나눈 나머지를 구하고, 이를 StringBuilder의 맨 앞에 삽입한다.
3. 입력값 x를 base로 나누는 과정을 반복한다.
4. 이 과정을 x가 0이 될 때까지 반복한다.
5. StringBuilder의 내용을 문자열로 반환한다.

이 과정을 거치면 입력값 x를 새로운 기