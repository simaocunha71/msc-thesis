你的代码逻辑是正确的，应该能够正确计算出字符串的长度。然而，问题可能出在输入部分。

在C++中，`cin`会读取输入直到遇到空白字符（如空格、制表符、换行符等）。因此，如果你在输入字符串后按下空格或者回车，`cin`会认为你已经结束了输入，并开始读取下一个输入。

在你的代码中，`cin>>str;`会读取一个单词，而不是整个字符串。如果你输入的是"abc"，然后按下空格或者回车，`cin`会读取"abc"并结束输入，然后`strlen(str)`会返回0，因为`str`现在是一个空字符串。

要解决这个问题，你可以使用`getline`函数来读取整行输入。`getline`会读取整行，包括空格和换行符。以下是修改后的代码：

```cpp
#include<stdio.h>
#include<string>
using namespace std;

int strlen(string str){
    int count = 0;
    for(int i = 0; i < str.size(); i++) {
        count++;
    }
    return count;
}

int main()
{
    string str;
    getline(cin, str);
    cout<<strlen(str)<<endl;
    return 0;
}
```

现在，如果你输入"abc"，然后按下回车，`getline`会读取整行，包括"abc"和回车，所以`strlen(str)`会返回3。