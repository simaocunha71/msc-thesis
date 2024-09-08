这段代码的问题在于它没有正确处理字符串长度不一致的情况。在C++中，字符串的长度可以通过`length()`函数获取，但是这个函数返回的是无符号整数类型。在`string_xor`函数中，`x`和`y`都被声明为`int`类型，但是当`x`或`y`为0时，它们会被自动转换为无符号整数类型。这可能会导致意外的行为，特别是在比较`x`和`y`时，因为`int`类型的比较与无符号整数类型的比较是不同的。

改正后的代码如下：

```cpp
#include<stdio.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
    int x = a.length();
    int y = b.length();
    int z = max(x, y);
    int arr1[z];
    int arr2[z];
    int arr3[z];
    for(int i = 0; i < z; i++){
        arr1[i] = 0;
        arr2[i] = 0;
        arr3[i] = 0;
    }
    for(int i = 0; i < x; i++){
        arr1[i] = a[i]-'0';
    }
    for(int i = 0; i < y; i++){
        arr2[i] = b