/*
Write a function that accepts a vector of strings as a parameter,
deletes the strings that have odd lengths from it,
and returns the resulted vector with a sorted order,
The vector is always a vector of strings and never a vector of numbers,
and it may contain duplicates.
The order of the vector should be ascending by length of each word, and you
should return the vector sorted by that rule.
If two words have the same length, sort the vector alphabetically.
The function should return a vector of strings in sorted order.
You may assume that all words will have the same length.
For example:
assert vector_sort({"aa", "a", "aaa"}) => {"aa"}
assert vector_sort({"ab", "a", "aaa", "cd"}) => {"ab", "cd"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> sorted_list_sum(vector<string> lst){
    vector<string> result;
    for(int i=0;i<lst.size();i++){
        if(lst[i].length()%2==0){
            result.push_back(lst[i]);
        }
    }
    sort(result.begin(),result.end());
    return result;
}
int main(){
    vector<string> lst={"aa", "a", "aaa"};
    vector<string> result=sorted_list_sum(lst);
    for(int i=0;i<result.size();i++){
        cout<<result[i]<<endl;
    }
    return 0;
}这是我的代码，但是没有通过测试
请问问题出在哪

你的代码没有通过测试的原因是，你的代码只考虑了长度为偶数的字符串，而没有删除长度为奇数的字符串。你的代码也没有对具有相同长度的字符串进行字母顺序排序。

以下是我对你的代码进行了修改，以使其符合要求：

```cpp
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> sorted_list_sum(vector<string> lst){
    vector<string> result;
    for(int i=0;i<lst.size();i++){
        if(lst[i].length()%2==0){
            result.push_back(lst[i]);
        }
    }
    sort(result.begin(),result.end(), [](string a, string b) {
        if (a.length() == b.length()) {
            return a < b;
        }
        return a.length() < b.length();
    });
    return result;
}
```

在这个修改后的代码中，我添加了一个lambda函数作为`sort`的第三个参数