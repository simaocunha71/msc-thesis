    vector<int> count(2, 0);
    for (int i = 1; i <= n; i++){
        string s = to_string(i);
        int j = 0, k = s.size() - 1;
        while (j < k){
            if (s[j++] != s[k--]) continue A;
        }
        if (s.size() % 2 == 0){
            count[0]++;
        }else{
            count[1]++;
        }
    }
    return count;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<int> result = even_odd_palindrome(n);
    printf("(%d, %d)", result[0], result[1]);
    return 0;
}
```

## 解题思路

使用暴力法解决问题，对于1到n之间的每个整数，判断它是否是回文数，然后根据其长度是偶数还是奇数，增加对应的计数器。

## 复杂度分析

时间复杂度为O(n^2)，因为对于从1到n的每个整数，我们都需要遍历其所有数字以判断它是否是回文数。空间复杂度为O(1)，因为我们只使用了固定数量的空间来存储计数器和整数值。

## 参考代码

这段代码是参考代码，它是正确的，但可能不是最优的。

```cpp
#include<vector>
#include<cmath>
using namespace std;

bool isPalindrome(int n) {
    int rev = 0; 
    int temp = n; 
    while (temp != 0) {
        rev = (rev * 10) + (temp % 10);
        temp = temp / 10;
    }
    return (rev == n);
}

vector<int> even_odd_palindrome(int n){
    vector<int> count(2, 0);
    for (int i = 1; i <= n; i++){
        if