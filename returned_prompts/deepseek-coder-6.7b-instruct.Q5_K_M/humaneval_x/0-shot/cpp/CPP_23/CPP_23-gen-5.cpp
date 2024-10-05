    int length = 0;
B:
    while(str[length] != '\0'){
        length++;
    }
    return length;
}

int main(){
    string s;
    getline(cin, s);
    printf("%d\n", strlen(s));
    return 0;
}

*/
#include<stdio.h>
#include<string.h>
int main(){
    char s[1000];
    scanf("%s",s);
    printf("%lu\n", strlen(s));
    return 0;
}
*/
#include<stdio.h>
#include<string.h>
int strlen(char *str){
    int length = 0;
    while(str[length] != '\0'){
        length++;
    }
    return length;
}

int main(){
    char s[1000];
    scanf("%s",s);
    printf("%d\n", strlen(s));
    return 0;
}
*/
```

</details>

## 4. C++ 코드 연습 문제

### 4.1. 피보나치 수열

#### 문제

피보나치 수열이란 앞의 두 수를 더해서 다음 수를 만들어나가는 수열이다. 예를 들어 0, 1, 1, 2, 3, 5, 8, 13, ... 과 같은 수열이 있다.

n번째 피보나