代码中的问题有以下几个：

1. 在函数`any_int`中，使用了`using namespace std;`，这是不必要的，因为该函数中没有使用C++标准库中的任何元素。

2. 在函数`any_int`中，使用了`float`类型的参数，但是在判断是否为整数时，使用了`int`类型的比较。这可能会导致类型不匹配的错误。应该使用`int`类型的参数，并在判断是否为整数时，将`float`类型的参数转换为`int`类型。

3. 在`main`函数中，使用了`scanf`函数来读取用户输入的三个数，但是没有检查输入是否成功。如果用户输入的不是数字，`scanf`函数会返回错误，并且不会修改`a`、`b`和`c`的值。应该使用`scanf`函数的返回值来检查输入是否成功。

4. 在`main`函数中，使用了`printf`函数来输出结果。但是，`printf`函数的参数是`"True"`和`"False"`，而不是`true`和`false`。应该使用`printf`函数的参数是`true`和`false`。

5. 在`main`函数中，使用了`printf`函数来输出结果。但是，`printf`函数的参数是`"True"`和`"False"`，而不是`true`和`false`。应该使用`printf`函数的参数是`true`和`false`。

6. 在`main`函数中，没有在`return 0;`之前使用`exit(0);`来结束程序的执行。这是不必要的，因为程序在`return 0;`之后会自然结束。

修改后的代码如下：

```c++
#include<stdio.h>
#include<math.h>
using namespace std;
bool any_int(int a,int b,int c){

    if(a+b