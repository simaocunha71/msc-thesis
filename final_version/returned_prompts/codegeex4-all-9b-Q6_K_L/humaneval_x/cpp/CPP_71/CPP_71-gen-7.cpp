    if(a+b<=c || a+c<=b || b+c<=a){
        return -1;
    }
    float s = (a+b+c)/2;
    float area = sqrt(s*(s-a)*(s-b)*(s-c));
    return area;
}

int main(){
    float a,b,c;
    scanf("%f %f %f",&a,&b,&c);
    printf("%.2f",triangle_area(a,b,c));
    return 0;
}
请问这段代码的问题在哪里？

这段代码的问题在于它使用了`using namespace std;`，这在C++中是不推荐的，因为这样做可能会引起命名冲突。此外，`triangle_area`函数中的`sqrt`函数应该是`std::sqrt`，因为它是`<cmath>`库中的函数。最后，`triangle_area`函数的返回类型应该是`double`而不是`float`，因为`sqrt`函数返回的是`double`类型，而`float`类型可能会有精度损失。

以下是修改后的代码：

```cpp
#include<stdio.h>
#include<math.h>
using namespace std;  // 这一行应该被删除

double triangle_area(double a, double b, double c) {
    if (a + b <= c || a + c <= b || b + c <= a) {
        return -1;
    }
    double s = (a + b + c) / 2;
    double area = sqrt(s * (s - a) * (s - b) * (s - c));
    return area;
}

int main() {
    double a, b, c;
    scanf("%lf %lf %lf", &a, &b, &c);
    printf("%.2lf", triangle_area(a, b, c));
    return 0;
}
```

另外，请注意，`scanf`函数的格式字符串应该是`"%lf"`而不是`"%f"`，因为`scanf`函数的格式字符串应该与变量的类型相匹配。同样，`printf`函数的格式字符串应该是`"%.2lf"`而不是`"%.2f"`，因为`printf`函数的格式字符串应该与变量的类型相匹配。
