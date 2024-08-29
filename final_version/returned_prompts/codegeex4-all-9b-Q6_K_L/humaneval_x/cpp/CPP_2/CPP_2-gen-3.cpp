你的代码总体上是正确的，但有一些小问题可以改进：

1. 你不需要使用`using namespace std;`，除非你在整个文件中都需要使用标准库中的元素。
2. 在`main`函数中，你可以直接使用`truncate_number`函数，而不需要声明`result`变量。
3. 你的代码中有一个`A:`标签，但在这个上下文中并没有使用它。如果你不打算使用它，可以删除它。
4. 在`printf`语句中，你可以使用`%.2f`来限制小数点后的位数，这样输出的结果会更清晰。

以下是改进后的代码：

```cpp
#include<stdio.h>
#include<math.h>

float truncate_number(float number){
    float num = number;
    int num2 = (int)num;
    float num3 = num - num2;
    return num3;
}

int main()
{
    float number = 3.5;
    float result = truncate_number(number);
    printf("The decimal part of the number is: %.2f\n", result);
    return 0;
}
```

这段代码应该能够正确地输出给定数字的小数部分。