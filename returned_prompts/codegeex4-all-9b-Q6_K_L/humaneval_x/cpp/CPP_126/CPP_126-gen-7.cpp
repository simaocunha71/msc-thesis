/*
Given a vector of numbers, return whether or not they are sorted
in ascending order. If vector has more than 1 duplicate of the same
number, return false. Assume no negative numbers and only integers.

Examples
is_sorted({5}) ➞ true
is_sorted({1, 2, 3, 4, 5}) ➞ true
is_sorted({1, 3, 2, 4, 5}) ➞ false
is_sorted({1, 2, 3, 4, 5, 6}) ➞ true
is_sorted({1, 2, 3, 4, 5, 6, 7}) ➞ true
is_sorted({1, 3, 2, 4, 5, 6, 7}) ➞ false
is_sorted({1, 2, 2, 3, 3, 4}) ➞ true
is_sorted({1, 2, 2, 2, 3, 4}) ➞ false
*/

#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
bool is_sorted(vector<int> lst){

    for(int i=0; i<lst.size()-1; i++){
        if(lst[i] > lst[i+1]){
            return false;
        }
    }

    for(int i=0; i<lst.size()-1; i++){
        if(lst[i] == lst[i+1]){
            return false;
        }
    }

    return true;
}
int main(){
    vector<int> v = {1, 3, 2, 4, 5, 6, 7};
    if(is_sorted(v)){
        printf("true");
    }else{
        printf("false");
    }
    return 0;
}
请问代码有什么问题吗？

代码的逻辑基本正确，但是有一个问题。当列表中存在两个连续的相同元素时，代码会返回`false`，因为这是不符合题目要求的。题目要求当列表中有超过一个相同的元素时，返回`false`，而不是在存在两个连续相同元素时返回`false`。

所以，当存在两个连续相同的元素时，我们应该继续检查下一个元素，而不是立即返回`false`。以下是修改后的代码：

```cpp
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
bool is_sorted(vector<int> lst){
    for(int i=0; i<lst