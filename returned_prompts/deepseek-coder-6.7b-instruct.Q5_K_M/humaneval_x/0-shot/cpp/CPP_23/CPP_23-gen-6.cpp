    int i = 0;
B:
    while(str[i] != '\0'){
        i++;
    }
    return i;
}

int main(){
    printf("%d\n", strlen(""));
    printf("%d\n", strlen("abc"));
    return 0;
}
```

## 4. 예제: 문자열 복사

```cpp
