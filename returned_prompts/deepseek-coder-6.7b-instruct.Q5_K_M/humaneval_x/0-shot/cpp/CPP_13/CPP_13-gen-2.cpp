    if(b==0)
        return a;
    else
        return greatest_common_divisor(b,a%b);
}
int main(){
    int a,b;
    printf("Enter two numbers: ");
    scanf("%d %d",&a,&b);
    printf("GCD of %d and %d is: %d",a,b,greatest_common_divisor(a, b));
    return 0;
}
```

这个程序使用欧几里得算法来找到两个数的最大公约数（GCD）。

它从两个输入数开始，并反复应用欧几里得算法的规则，直到第二个数（b）变为零。此时，第一个数（a）就是最大公约数。

以下是欧几里得算法的工作原理：

1. 如果 b 是 0，则 gcd(a, b) 就是 a，因为 gcd(a, 0) = a。
2. 如果 b 不是 0，则 gcd(a, b) 就是 gcd(b, a mod b)。

这个算法的原理是，两个数 a 和 b 的最大公约数不会改变，即使我们将 a 替换为 b，将 b 替换为 a mod b。

这个算法通过递归实现，直到 b 变为 0。

这个算法的时间复杂度是 O(log min(a, b))，这是因为我们每次递归调用都将输入数缩小一半。

这个算法的空间复杂度是 O(1)，因为我们只使用了常数空间来存储 a 和 b。

注意：这个程序使用了 C 语言，不是 C++。

如果你需要在 C++ 中实现这个算法，只需将 C 语言的 printf 和 scanf 替换为 C++ 的 cout 和 cin，并将 return 0; 替换为 return 0;。

如果你需要在其他语言中实现这个算法，你可以参考这个算法的描述，并使用该语言的基本语法和函数调用机制来实现。

