```cpp
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> sort_third(vector<int> l) {
    vector<int> res;
    vector<int> third;
    for(int i = 0; i < l.size(); i++) {
        if(i%3==0) third.push_back(l[i]);
        else res.push_back(l[i]);
    }
    sort(third.begin(),third.end());
    for(int i = 0; i < third.size(); i++) {
        res.insert(res.begin()+i*3,third[i]);
    }
    return res;
}

int main() {
    vector<int> v = {5, 6, 3, 4, 8, 9, 2};
    vector<int> res = sort_third(v);
    for(int i = 0; i < res.size(); i++) {
        cout << res[i] << " ";
    }
    cout << endl;
    return 0;
}
```

解释：
1. 首先创建两个vector，res用于存储不是3的倍数的元素，third用于存储是3的倍数的元素。
2. 遍历输入的vector，如果是3的倍数，则将其存入third，否则存入res。
3. 对third进行排序。
4. 遍历third，将排序后的元素插入到res的对应位置。
5. 返回res。