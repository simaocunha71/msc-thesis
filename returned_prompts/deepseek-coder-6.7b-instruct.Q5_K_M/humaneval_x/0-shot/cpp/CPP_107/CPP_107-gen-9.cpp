    vector<int> res(2, 0);
    for(int i = 1; i <= n; i++){
D:
        string s = to_string(i);
        string r = s;
        reverse(r.begin(), r.end());
        if(s == r){
            if(i % 2 == 0)
                res[0]++;
            else
                res[1]++;
        }
    }
    return res;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> res = even_odd_palindrome(n);
    printf("(%d, %d)", res[0], res[1]);
    return 0;
}
/*
Output:
(4, 6)
*/
```

## 3. 优化后的算法
```cpp
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

bool isPalindrome(int num) {
    string original = to_string(num);
    string reversed = original;
    reverse(reversed.begin(), reversed.end());
    return original == reversed;
}

vector<int> even_odd_palindrome(int n) {
    vector<int> result(2, 0);
    for (int i = 1; i <= n; i++) {
        if (isPalindrome(i)) {
            if (i % 2 == 0) {
                result[0] += 1;
            } else {
                result[1] += 1;
            }
        }
    }
    return result;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> res = even_odd_palindrome(n);
    printf("(%d, %d)", res[0], res[1]);
    return 0;
}
```

## 4. 算法复杂度

该算法的复杂度为O(n^2)，因为在最坏的情况下，我们需要遍历每个数字，并检查其是否为