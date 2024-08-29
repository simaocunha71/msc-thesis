#include <iostream>
using namespace std;
int main() {
    int n = 5;
    string result = "";
    for (int i = 0; i <= n; i++) {
        result += to_string(i) + " ";
    }
    result.pop_back();  // remove the trailing space
    cout << result << endl;
    return 0;
}
请问哪个更优？为什么

你的A代码更优，因为它使用了标准库的`string`类，而你的Q代码使用了C语言的`printf`函数。

使用标准库的`string`类可以避免手动管理字符串的内存，减少出错的可能性，并且提供了一些方便的字符串操作函数，如`+`操作符用于字符串连接，`pop_back`函数用于移除最后一个字符等。

相比之下，C语言的`printf`函数虽然简单，但需要手动管理字符串的内存，并且在处理字符串时需要特别注意字符数组的边界，容易出错。此外，C语言的`printf`函数没有提供方便的字符串操作函数，需要自己实现或使用其他库。

因此，建议使用标准库的`string`类来处理字符串操作，以提高代码的可读性和可维护性。
