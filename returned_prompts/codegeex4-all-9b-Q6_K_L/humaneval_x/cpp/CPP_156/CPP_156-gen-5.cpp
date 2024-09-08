当然可以！你可以使用以下代码将一个正整数转换为罗马数字：

```cpp
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

string int_to_mini_romank(int number){

    vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> symbols = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};

    string result = "";
    for (int i = 0; i < values.size(); i++) {
        while (number >= values[i]) {
            number -= values[i];
            result += symbols[i];
        }
    }
    return result;
}
```

你可以将这个函数添加到你的代码中，并调用它