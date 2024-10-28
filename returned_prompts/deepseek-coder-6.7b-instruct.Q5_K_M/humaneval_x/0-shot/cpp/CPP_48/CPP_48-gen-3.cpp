    int i = 0;
    int j = text.length() - 1;
    while(i < j){
        if(text[i] != text[j]){
            return false;
        }
        i++;
        j--;
    }
    return true;
}

int main(){
    printf("%s\n", is_palindrome("") ? "true" : "false");
    printf("%s\n", is_palindrome("aba") ? "true" : "false");
    printf("%s\n", is_palindrome("aaaaa") ? "true" : "false");
    printf("%s\n", is_palindrome("zbcd") ? "true" : "false");
    return 0;
}
```

#### Python

```python
