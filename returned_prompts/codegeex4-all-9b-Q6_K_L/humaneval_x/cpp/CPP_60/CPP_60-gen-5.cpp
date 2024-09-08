你的代码基本上是正确的，但是有一个小问题。当 `n` 等于 0 时，你的代码应该返回 0，但是在你的代码中，当 `n` 等于 0 时，你的代码会返回 `0+n`，这实际上是 0。所以你的代码应该返回 0，而不是 `0+n`。所以你应该把你的代码中的 `return n+sum_to_n(n-1);` 改为 `return n+sum_to_n(n-1);`。

这是修正后的代码：

```c
#include<stdio.h>
using namespace std;
int sum_to_n(int n){
    if(n==0){
        return 0;
    }
    else{
        return n+sum_to_n(n-1);
    }
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%d\n",sum_to_n(n));
    return 0;
}
```

另外，你的代码中有一个小错误。在 `main` 函数中，你应该使用 `cin` 来读取输入，而不是 `scanf`。所以你应该把你的代码中的 `scanf("%d",&n);` 改为 `cin>>n;`。

这是修正后的代码：

```c
#include<stdio.h>
using namespace std;
int sum_to_n(int n){
    if(n==0){
        return 0;
    }
    else{
        return n+sum_to_n(n-1);
    }
}

int main(){
    int n;
    cin>>n;
    printf("%d\n",sum_to_n(n));
    return 0;
}
```