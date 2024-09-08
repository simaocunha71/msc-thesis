这段代码在逻辑上是正确的，可以正确地计算两个字符串的异或值。然而，它没有处理字符串长度不一致的情况，比如"01"和"110"这样的输入。在这种情况下，代码会尝试访问不存在的字符，导致未定义的行为。

为了解决这个问题，我们可以添加一些检查，确保两个字符串长度相同。如果它们长度不同，我们可以在较短的字符串前面添加足够的"0"来使其长度与较长的字符串相同。这样，我们可以确保在计算异或值时不会访问不存在的字符。

下面是修改后的代码：

```cpp
#include<stdio.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
    int len_a = a.length();
    int len_b = b.length();
    if(len_a < len_b){
        a = string(len_b - len_a, '0') + a;
    }else if(len_b < len_a){
        b = string(len_a - len_b, '0') + b;
    }
    string result="";
    for (int i=0;i<a.length();i++){
        if (a[i]!=b[i]){
            result=result+"1";
        }
        else{
            result=result+"0";
        }
    }
    return result;
}
```

在这个修改后的版本中，我们首先比较两个字符串的长度。如果它们长度不同，我们在较短的字符串前面添加足够的"0"来使其长度与较长的字符串相同。这样，我们可以确保在计算异或值时不会访问不存在的字符。