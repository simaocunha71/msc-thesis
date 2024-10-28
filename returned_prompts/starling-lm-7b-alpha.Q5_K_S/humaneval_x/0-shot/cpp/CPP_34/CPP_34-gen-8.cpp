
这道题是要求求一个向量的不重复的元素并进行排序。

首先，我们需要对这个向量进行排序，这样我们才能判断后面的元素是否是重复的。

然后我们遍历这个排序后的向量，如果当前元素和上一个元素不相等，我们就将其加入到新的向量中。

最后，我们返回新的向量即可。

这样，就能够求出一个向量的不重复的元素并进行排序了。

代码如下：

```cpp
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> unique(vector<int> l){

    sort(l.begin(), l.end());
    vector<int> r;
    for(int i = 0; i < l.size(); i++)
        if(i == 0 || l[i] != l[i-1])
            r.push_back(l[i]);
    return r;
}

int main(){

    vector<int> l;
    while(1){
