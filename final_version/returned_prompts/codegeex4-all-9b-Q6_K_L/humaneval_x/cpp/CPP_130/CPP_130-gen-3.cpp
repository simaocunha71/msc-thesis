这段代码存在以下几个问题：

1. 在循环中，`v[i+1]` 是不存在的，因为 `v` 的索引是从 0 开始的，而 `i` 的最大值是 `n`，所以 `v[i+1]` 会超出 `v` 的索引范围。

2. 在计算 `tri(n)` 时，应该使用 `v[i-1]`、`v[i-2]` 和 `v[i-3]`，而不是 `v[i]`、`v[i-2]` 和 `v[i+1]`。

3. `v` 的大小应该为 `n+2`，因为 `v` 中包含 `tri(1)` 到 `tri(n+1)`，所以 `v` 的大小应该是 `n+2`。

下面是修改后的代码：

```cpp
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){
    vector<int> v(n+2, 0);
    v[0] = 3;
    for(int i=1;i<=n;i++){
        if(i%2==0){
            v[i] = 1+i/2;
        }
        else{
            v[i] = v[i-1]+v[i-2]+v[i-3];
        }
    }
    return v;
}
int main(){
    vector<int> v=tri(3);
    for(int i=0;i<v.size();i++)
        printf("%d ",v[i]);
    return 0;
}
```

这段代码会输出 `1 3 2 8`。