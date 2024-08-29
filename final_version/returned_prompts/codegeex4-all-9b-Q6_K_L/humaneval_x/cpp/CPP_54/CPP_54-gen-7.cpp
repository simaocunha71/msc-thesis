    if(s0.length()==s1.length()){
        sort(s0.begin(),s0.end());
        sort(s1.begin(),s1.end());
        if(s0==s1)
            return true;
        else
            return false;
    }
    else
        return false;
}
int main(){
    string a="eabcdzzzz",b="dddzzzzzzzddeddabc";
    printf("%d\n",same_chars(a,b));
    return 0;
}
为什么报错？

在C++中，`printf`函数不能直接打印`bool`类型的值。你需要使用`%d`来打印`bool`类型的值，它会将`true`打印为`1`，将`false`打印为`0`。

在你的代码中，你可以将`printf("%d\n",same_chars(a,b));`修改为`printf("%d\n",same_chars(a,b)?1:0);`。这样，如果`same_chars(a,b)`返回`true`，`printf`会打印`1`；如果返回`false`，`printf`会打印`0`。

修改后的代码如下：

```cpp
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
bool same_chars(string s0,string s1){

    if(s0.length()==s1.length()){
        sort(s0.begin(),s0.end());
        sort(s1.begin(),s1.end());
        if(s0==s1)
            return true;
        else
            return false;
    }
    else
        return false;
}
int main(){
    string a="eabcdzzzz",b="dddzzzzzzzddeddabc";
    printf("%d\n",same_chars(a,b)?1:0);
    return 0;
}
```

这样，你的代码应该就可以正确地运行了。