    int fibo(int n){
        if (n<=1)
            return n;
        else
            return fibo(n-1)+fibo(n-2);
    }

    int prime(int n){
        if (n<=1)
            return 0;
        for(int i = 2; i*i <=n; i++){
            if(n%i == 0)
                return 0;
        }
        return 1;
    }

    int count = 0;
    int num = 0;

    while(count < n){
        num++;
        if(prime(fibo(num))){
            count++;
        }
    }

    return fibo(num);
}

int main(){
    printf("%d\n", prime_fib(1));
    printf("%d\n", prime_fib(2));
    printf("%d\n", prime_fib(3));
    printf("%d\n", prime_fib(4));
    printf("%d\n", prime_fib(5));
    return 0;
}
```

### 解答
```cpp
#include<iostream>
#include<vector>
using namespace std;

int prime_fib(int n){
    vector<int> fibo{0, 1};
    vector<int> prime{0, 1};

    for(int i = 2; ; i++){
        fibo.push_back(fibo[i-1]+fibo[i-2]);
        prime.push_back(0);

        if(fibo[i] > 1){
            prime[fibo[i]] = prime[fibo[i-1]] + prime[fibo[i-2]];
        }

        if(prime[i] > 1){
            prime[i] = prime[i-1] + prime[i-2];
        }

        if(prime[fibo[i]] && fibo[i] > 1){
            prime[i] = prime[i-1] - prime[fib