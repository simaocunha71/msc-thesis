    string result = "";
    while(x > 0){
        result = to_string(x%base) + result;
        x /= base;
    }
    return result;
}
int main(){
    printf("%s\n", change_base(8, 3).c_str());
    printf("%s\n", change_base(8, 2).c_str());
    printf("%s\n", change_base(7, 2).c_str());
    return 0;
}

*/

int main(){
    printf("%s\n", change_base(8, 3).c_str());
    printf("%s\n", change_base(8, 2).c_str());
    printf("%s\n", change_base(7, 2).c_str());
    return 0;
}
```

## 参考答案
```cpp
#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string result = "";
    while(x > 0){
        result = to_string(x%base) + result;
        x /= base;
    }
    return result;
}
int main(){
    printf("%s\n", change_base(8, 3).c_str());
    printf("%s\n", change_base(8, 2).c_str());
    printf("%s\n", change_base(7, 2).c_str());
    return 0;
}
```

## 运行结果

```
22
1000
111
```

## 参考链接

[C++中的string和to_string函数](https://www.geeksforgeeks.org/string-to_string-in-c/)

## 相关题目

[C++中的字符串操作](https://www.nowcoder.com/questionTerminal/6e643f61e6c04e8fa5f5d45b9c91359c)

[C++中的字符串拼接](https://www.