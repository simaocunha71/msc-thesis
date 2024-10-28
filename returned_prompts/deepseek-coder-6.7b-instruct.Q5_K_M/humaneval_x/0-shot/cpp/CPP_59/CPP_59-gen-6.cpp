    for (int i = 2; i*i <= n; ++i){
        while (n % i == 0){
            n /= i;
        }
    }
B:
    return n;
}
int main(){
    printf("%d", largest_prime_factor(13195));
    return 0;
}
```

### Question 4

```c++
