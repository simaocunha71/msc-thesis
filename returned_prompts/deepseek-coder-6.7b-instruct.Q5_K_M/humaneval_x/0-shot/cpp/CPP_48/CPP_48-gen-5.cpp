    int length = text.size();
    for(int i=0; i<length/2; i++){
        if(text[i] != text[length-i-1]){
            return false;
        }
    }
    return true;
}
int main() {
    printf("%s\n", is_palindrome("") ? "true" : "false");
    printf("%s\n", is_palindrome("aba") ? "true" : "false");
    printf("%s\n", is_palindrome("aaaaa") ? "true" : "false");
    printf("%s\n", is_palindrome("zbcd") ? "true" : "false");
    return 0;
}
```

## 3.1.2. 문자열 길이 구하기

