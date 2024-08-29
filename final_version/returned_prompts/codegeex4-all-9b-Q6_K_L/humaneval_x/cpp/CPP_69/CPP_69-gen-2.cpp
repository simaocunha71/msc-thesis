#include <iostream>
#include <vector>
#include <map>
using namespace std;

int search(vector<int> lst) {
    map<int, int> count;
    for (int i = 0; i < lst.size(); i++) {
        count[lst[i]]++;
    }
    int res = -1;
    for (auto &p : count) {
        if (p.second >= p.first) {
            res = max(res, p.first);
        }
    }
    return res;
}

int main() {
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    cout << search(lst) << endl; // 2
    lst = {1, 2, 2, 3, 3, 3, 4, 4, 4};
    cout << search(lst) << endl; // 3
    lst = {5, 5, 4, 4, 4};
    cout << search(lst) << endl; // -1
    return 0;
}
这个代码应该怎么优化

你的代码已经是一个很好的解决方案。它通过一个map来记录每个数字的频率，然后遍历这个map，找到频率大于等于数字本身的最大的数字。

如果你想进一步优化，可以考虑以下几点：

1. **减少不必要的内存分配**：在你的代码中，你创建了一个map来存储每个数字的频率。但是，如果输入的数字范围很大，这个map可能会占用大量的内存。你可以尝试使用一个固定大小的数组来代替map，因为你的输入数字都是正整数。

2. **减少遍历次数**：在你的代码中，你首先遍历了整个输入列表来创建map，然后又遍历了整个map来找到答案。你可以尝试将这两个步骤合并，只遍历一次输入列表。

以下是使用固定大小数组的优化代码：

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int search(vector<int> lst) {
    const int MAX_NUM = 1000; // 假设最大数字不超过1000
    int count[MAX_NUM + 1] = {0};
    int res = -1;
    for (int i = 0; i < lst.size(); i++) {
        count[lst[i]]++;
        if (lst[i] <= MAX_NUM && count[lst[i]] >= lst[i]) {
            res = max(res, lst[i]);
       