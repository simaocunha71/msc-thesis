这段代码是正确的。它使用C++标准库中的`string`类和`size()`方法来计算字符串的长度。`strlen(str)`返回`str`的长度，然后在`main()`函数中打印出来。

这里是完整的代码：

```cpp
#include<iostream>
#include<string>
using namespace std;

int strlen(string str){
    return str.size();
}

int main(){
    string str="Hello World";
    cout << strlen(str) << endl;
    return 0;
}
```

输出结果为：11，因为"Hello World"的长度是11。