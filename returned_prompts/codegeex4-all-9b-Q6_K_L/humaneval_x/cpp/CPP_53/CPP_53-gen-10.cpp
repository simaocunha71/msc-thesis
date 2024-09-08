这段代码有一些问题需要修正：

1. `#include<stdlib.h>` 应该是 `#include<stdlib.h>`，注意 `stdlib.h` 中的 `l` 应该是大写。
2. `using namespace std;` 这一行是不必要的，因为这段代码没有使用 C++ 标准库中的任何东西。
3. `add` 函数的返回类型应该是 `void` 而不是 `int`，因为函数没有返回值。
4. `printf` 函数的返回值没有被使用，应该将其赋值给一个变量。
5. 在 `main` 函数中，`add` 函数的返回值没有被使用，应该将其赋值给一个变量。

以下是修正后的代码：

```c
#include<stdio.h>
#include<stdlib.h>

void add(int x, int y) {
    printf("%d", x + y);
}

int main() {
    int x, y;
    scanf("%d%d", &x, &y);
    add(x, y);
    return 0;
}
```