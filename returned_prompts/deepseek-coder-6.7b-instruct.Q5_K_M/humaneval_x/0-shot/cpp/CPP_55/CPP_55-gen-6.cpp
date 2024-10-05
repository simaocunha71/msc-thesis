  /*
  fib(1)=1
  fib(2)=1
  fib(n)=fib(n-1)+fib(n-2)
  */
  if(n==1 || n==2){
    return 1;
  }
  else{
    return fib(n-1)+fib(n-2);
  }
}
int main() {
    printf("%d\n", fib(10));
    printf("%d\n", fib(1));
    printf("%d\n", fib(8));
    return 0;
}
```

## 3. 斐波那契数列的记忆化

斐波那契数列的递归计算虽然可行，但是效率低下，因为存在重复计算的问题。我们可以通过一种叫做记忆化的技术来解决这个问题，即我们存储已经计算过的结果，避免重复计算。

```cpp
#include<stdio.h>
#include<vector>
using namespace std;

int fib(int n, vector<int>& memo){
    if(n == 1 || n == 2) {
        return 1;
    }
    if(memo[n] != 0) {
        return memo[n];
    }
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
    return memo[n];
}

int main() {
    vector<int> memo(11, 0);
    printf("%d\n", fib(10, memo));
    return 0;
}
```

## 4. 动态规划

我们可以使用动态规划来解决这个问题，通过迭代的方式来计算斐波那契数列。

```cpp
#include<stdio.h>
#include<vector>
using namespace std;

int fib(int n){
    if(n <= 2){
        return 1;
    }
    vector<int> dp(n + 1);
    dp[1] = dp[2] = 1;
    for(int i = 3; i <=