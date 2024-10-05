    if(a==0)
        return b;
B:
    return greatest_common_divisor(b%a, a);
}

int main(){
    int a = 25, b = 15;
    printf("%d", greatest_common_divisor(a, b));
    return 0;
}
```

### 4. 判断一个数是否是质数

```cpp
