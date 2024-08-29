这段代码的问题在于，它使用了递归来实现从1到n的求和，但是递归调用没有正确实现，并且在递归中使用了局部变量sum，这会导致每次递归调用时sum都被重新初始化为0，从而导致求和结果不正确。正确的实现应该是使用循环来计算从1到n的求和，而不是使用递归。下面是修正后的代码：
```c++
#include<stdio.h>
using namespace std;
int sum_to_n(int n){
    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}
int main(){
    int n;
    scanf("%d",&n);
    printf("%d",sum_to_n(n));
    return 0;
}
```