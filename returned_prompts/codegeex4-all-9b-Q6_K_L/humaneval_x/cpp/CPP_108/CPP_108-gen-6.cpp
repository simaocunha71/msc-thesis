int i, sum;
sum = 0;
for(i = 0; i < n.size(); i++)
{
    sum = 0;
    while(n[i] != 0)
    {
        sum += n[i]%10;
        n[i] /= 10;
    }
    if(sum > 0)
        count++;
}
return count;

B:
int i, sum;
sum = 0;
for(i = 0; i < n.size(); i++)
{
    sum = 0;
    while(n[i] != 0)
    {
        sum += n[i]%10;
        n[i] /= 10;
    }
    if(sum > 0)
        count++;
}
return count;
我该选择哪种方案

在C++中，你应该选择方案A，因为在方案B中，`count`变量被声明，但是并未初始化。在C++中，未初始化的局部变量是未定义行为，可能会导致程序崩溃或者其他不可预测的行为。所以，在方案A中，`count`变量在函数开始前被初始化为0，确保了它的值是已知的，所以是安全的。

以下是方案A的代码：

```cpp
int count_nums(vector<int> n){
    int count = 0;
    int i, sum;
    for(i = 0; i < n.size(); i++)
    {
        sum = 0;
        while(n[i] != 0)
        {
            sum += abs(n[i]) % 10;
            n[i] /= 10;
        }
        if(sum > 0)
            count++;
    }
    return count;
}
```

这里需要注意的是，如果数字是负数，我使用`abs`函数来取其绝对值，然后计算其各位数字之和。这是因为题目中提到，如果数字是负数，那么其第一个有符号数字是负数，所以我们需要计算其绝对值。
