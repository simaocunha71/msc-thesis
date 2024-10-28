  string str = "";
  for (int i = 0; i <= n; i++){
    str += to_string(i);
    if (i < n) str += " ";
  }
  return str;
}

int main(){
  int n;
  scanf("%d", &n);
  printf("%s", string_sequence(n).c_str());
  return 0;
}
```

## 代码解析

这段代码定义了一个函数`string_sequence`，它接受一个整数`n`作为输入，生成从0到`n`的数字字符串，并返回这个字符串。在这个函数中，我们首先初始化一个空字符串`str`。然后，我们使用一个for循环来遍历从0到`n`的所有数字。在每次循环迭代中，我们将当前数字转换为字符串，并将其附加到`str`中。如果当前数字不是`n`，我们将附加一个空格。循环结束后，我们返回`str`。

在`main`函数中，我们首先读取一个整数`n`，然后调用`string_sequence`函数，并打印返回的字符串。

## 测试

```
输入: 5
输出: "0 1 2 3 4 5"
```

```
输入: 0
输出: "0"
```

```
输入: 10
输出: "0 1 2 3 4 5 6 7 8 9 10"
```

## 注意

这个函数在输入数字很大的情况下可能会有问题，因为它可能会生成一个非常长的字符串。

## 参考

- [C++](https://en.cppreference.com/)
- [C++ string to_string() function](https://www.cplusplus.com/reference/string/to_string/)
- [C++ string append() function](https://www.cplusplus.com/reference/string/string/append/)
- [C++ string c_str() function](https://www.cplus