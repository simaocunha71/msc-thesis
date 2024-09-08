```cpp
#include<stdio.h>
#include<vector>
using namespace std;
int sum_squares(vector<int> lst){
    int sum = 0;
    for(int i=0; i<lst.size(); i++){
        if(i%3 == 0){
            lst[i] = lst[i]*lst[i];
        }
        if(i%4 == 0 && i%3 != 0){
            lst[i] = lst[i]*lst[i]*lst[i];
        }
        sum += lst[i];
    }
    return sum;
}
```
这个函数会对向量中的每一个元素进行操作，如果它的索引是3的倍数，那么这个元素会被平方，如果它的索引是4的倍数且不是3的倍数，那么这个元素会被立方。最后，函数