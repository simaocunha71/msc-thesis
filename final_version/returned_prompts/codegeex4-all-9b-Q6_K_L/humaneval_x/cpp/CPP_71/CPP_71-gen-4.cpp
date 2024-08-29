    if(a>0&&b>0&&c>0){
        if(a+b>c&&a+c>b&&b+c>a){
            float s=(a+b+c)/2;
            float area=sqrt(s*(s-a)*(s-b)*(s-c));
            return area;
        }
        else{
            return -1;
        }
    }
    else{
        return -1;
    }
}
int main(){
    float a,b,c;
    printf("Enter three sides of a triangle:");
    scanf("%f%f%f",&a,&b,&c);
    printf("%0.2f",triangle_area(a,b,c));
    return 0;
}
请问这段代码有什么问题？

这段代码的主要问题是，它试图使用C++的命名空间 `using namespace std;`，但是在C文件中（由 `.c` 或 `.h` 扩展名标识）这是不允许的。C++代码应该放在 `.cpp` 文件中，而C代码应该放在 `.c` 文件中。

另外，函数 `triangle_area` 的返回类型应该是 `double` 而不是 `float`，因为三角形的面积可能是小数。

最后，`scanf` 函数在读取浮点数时，应该使用 `%f` 而不是 `%f%f%f`。所以，你应该将 `scanf("%f%f%f",&a,&b,&c);` 改为 `scanf("%f %f %f",&a,&b,&c);`，并在输入时在三个数之间添加空格。

这是修正后的代码：

```c
#include<stdio.h>
#include<math.h>

double triangle_area(double a,double b,double c){
    if(a>0&&b>0&&c>0){
        if(a+b>c&&a+c>b&&b+c>a){
            double s=(a+b+c)/2;
            double area=sqrt(s*(s-a)*(s-b)*(s-c));
            return area;
        }
        else{
            return -1;
        }
    }
    else{
        return -1;
    }
}

int main(){
    double a,b,c;
    printf("Enter three sides of a triangle:");
    scanf("%lf %lf %lf",&a,&b,&c);
    printf("%0.2f",triangle_area(a,b,c));
    return 0;
}
```

这段代码现在应该可以正确地计算三角形的面积，并将其四舍五入到两位小数。如果输入的三个数不能