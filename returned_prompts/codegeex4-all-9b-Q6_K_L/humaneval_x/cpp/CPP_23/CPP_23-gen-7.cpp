/*
Return length of given string
>>> strlen("")
0
>>> strlen("abc")
3
*/
#include<stdio.h>
#include<cstring>
using namespace std;
int strlen(string str){
    return str.length();
}

B:
/*
Return length of given string
>>> strlen("")
0
>>> strlen("abc")
3
*/
#include<stdio.h>
#include<string>
using namespace std;
int strlen(string str){
    return str.size();
}

C:
/*
Return length of given string
>>> strlen("")
0
>>> strlen("abc")
3
*/
#include<stdio.h>
#include<cstring>
using namespace std;
int strlen(string str){
    return strlen(str);
}

D:
/*
Return length of given string
>>> strlen("")
0
>>> strlen("abc")
3
*/
#include<stdio.h>
#include<string>
using namespace std;
int strlen(string str){
    return sizeof(str);
}

选项 B 是正确的。

解释：

在 C++ 中，`string` 类型的 `length()` 函数返回字符串的长度（字符数）。因此，`strlen` 函数可以定义为 `str.length()`。

选项 A 和选项 B 的区别在于，`size()` 函数也是 `string` 类的一个成员函数，它也返回字符串的长度。然而，`size()` 函数可以用于 `string` 类型的迭代器，而 `length()` 函数不能。因此，`size()` 函数的适用性更广。

选项 C 是错误的。`strlen()` 函数是 C 标准库中的一个函数，它用于计算 C 风格字符串的长度。然而，`strlen()` 函数不能用于 `string` 类型的对象。

选项 D 是错误的。`sizeof()` 运算符用于返回变量或类型的大小（以字节为单位）。然而，`sizeof()` 运算符不能用于 `string` 类型的对象。`sizeof()` 运算符返回的是 `string` 类型的对象在内存中的大小，而不是字符串的长度。
