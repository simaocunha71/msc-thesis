    int counter = 0;
    for(char& c : brackets){
        if(c == '(') {
            counter++;
        } else if(c == ')') {
            counter--;
            if(counter < 0){
                return false;
            }
        }
    }
    return counter == 0;
}

int main(){
    printf("%d\n", correct_bracketing("("));
    printf("%d\n", correct_bracketing("()"));
    printf("%d\n", correct_bracketing("(()())"));
    printf("%d\n", correct_bracketing(")(()"));
    return 0;
}
```

## 문제 설명

주어진 문자열이 제대로 괄호가 열렸는지 확인하는 프로그램을 작성하라.

## 입력

문자열 하나가 주어진다. 문자열의 길이는 최대 1,000이다. 문자열은 '('와 ')'로만 이루어져 있다.

## 출력

제대로 괄호가 열렸으면 "1", 아니면 "0"을 출력한다.

## 예제 입력

```
(
()
(()())
)(()
