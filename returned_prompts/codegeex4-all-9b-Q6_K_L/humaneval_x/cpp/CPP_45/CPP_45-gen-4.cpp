这个程序不能输出结果的原因是因为在 `main` 函数中，`goto` 语句被用来跳转到 `A` 标签，而 `A` 标签处的 `if` 语句会检查 `a` 和 `h` 是否小于等于 0。如果 `a` 或 `h` 小于等于 0，程序会再次跳转到 `A` 标签，导致无限循环。

为了解决这个问题，可以在 `goto` 语句之前添加一个 `break` 语句，这样当 `a` 或 `h` 小于等于 0 时，程序会退出循环。另外，也可以在 `goto` 语句之后添加一个 `return` 语句，这样当 `a` 或 `h` 小于等于 0 时，程序会直接返回，不再执行 `goto` 语句。

以下是修改后的代码：

```c++
#include<stdio.h>
#include<math.h>
using namespace std;
float triangle_area(float a,float h){
    float area=(a*h)/2;
    return area;
}
int main()
{
    float a,h;
    printf("Enter the side and high of triangle:");
    scanf("%f%f",&a,&h);
    if(a<=0||h<=0)
    {
        printf("Side and high must be greater than 0.\n");
        return 0;
    }
    printf("area of triangle is %f",triangle_area(a,h));
    return 0;
}
```