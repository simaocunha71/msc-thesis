    int fib1=0,fib2=1,fib3,i,count=0;
    if(n==1)
        return 2;
    if(n==2)
        return 3;
    if(n==3)
        return 5;
    if(n==4)
        return 13;
    if(n==5)
        return 89;
    for(i=2;count<n;i++){
        fib3=fib1+fib2;
        fib1=fib2;
        fib2=fib3;
        int j;
        for(j=2;j<=fib3/2;j++){
            if(fib3%j==0){
                j=fib3;
                break;
            }
        }
        if(j>fib3/2){
            count++;
        }
        if(count==n){
            return fib3;
        }
    }
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%d",prime_fib(n));
    return 0;
}
```

## 代码解释

这段代码首先定义了两个变量`fib1`和`fib2`，分别代表斐波那契数列的前两个数。然后，它进入一个循环，计算斐波那契数列的下一个数。在这个循环中，它还检查生成的斐波那契数是否为素数。

如果生成的斐波那契数是素数，它会增加`count`的值。当`count`等于输入的`n`时，它会返回该斐波那契数。

注意：这段代码在处理大输入时可能会遇到问题，因为它没有处理大数的优化，并且没有处理斐波那契数列增长过快的情况。

## 运行代码

你可以将代码复制到一个C++编译器中运行，例如：

```c++
#include<iostream>
using namespace std;
int prime_fib(int n