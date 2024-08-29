```cpp
vector<int> sort_third(vector<int> l) {
    vector<int> res;
    vector<int> divisible_by_three;
    for (int i = 0; i < l.size(); i++) {
        if (i % 3 == 0) {
            divisible_by_three.push_back(l[i]);
        } else {
            res.push_back(l[i]);
        }
    }
    sort(divisible_by_three.begin(), divisible_by_three.end());
    for (int i = 0; i < divisible_by_three.size(); i++) {
        res.insert(res.begin() + i * 3, divisible_by_three[i]);
    }
    return res;
}
```

这个函数接收一个向量 l，并返回一个向量 l'，使得 l' 在不能被 3 整除的索引中与 l 相同，而在可以被 3 整除的索引中，其值等于 l 对应索引的值，但已排序。
```cpp
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> sort_third(vector<int> l) {
    vector<int> res;
    vector<int> divisible_by_three;
    for (int i = 0; i < l.size(); i++) {
        if (i % 3 == 0) {
            divisible_by_three.push_back(l[i]);
        } else {
            res.push_back(l[i]);
        }
    }
    sort(divisible_by_three.begin(), divisible_by_three.end());
    for (int i = 0; i < divisible_by_three.size(); i++) {
        res.insert(res.begin() + i * 3, divisible_by_three[i]);
    }
    return res;
}
```