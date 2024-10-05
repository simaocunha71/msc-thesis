  string str = "";
  for(int i=0; i<=n; i++){
    str += to_string(i);
    str += " ";
  }
  str.pop_back();
  return str;
}

int main(){
    printf("%s\n", string_sequence(0).c_str());
    printf("%s\n", string_sequence(5).c_str());
    return 0;
}
```

## 题目描述

给定一个整数 `n`，返回一个字符串，其中包含从 0 到 `n`（包括 `n`）的数字，以空格分隔。

示例：

```
输入：0
输出："0"

输入：5
输出："0 1 2 3 4 5"
```

## 解析

这个问题可以通过使用简单的循环来解决。我们将从 0 到 `n` 的每个数字转换为字符串，然后用空格连接起来。

```
function string_sequence(n) {
  let str = "";
  for(let i = 0; i <= n; i++) {
    str += i + " ";
  }
  return str.trim();
}
```

在这个函数中，我们初始化一个空字符串 `str`，然后从 0 到 `n` 的每个数字 `i` 都被添加到 `str` 中。在每个数字后面添加一个空格。最后，我们使用 `trim()` 函数去除末尾的空格，并返回结果字符串 `str`。

这个解决方案的时间复杂度是 O(n)，因为我们需要遍历从 0 到 `n` 的每个数字。空间复杂度也是 O(n)，因为我们将所有数字都存储在结果字符串中。

## 测试

你可以使用以下代码测试这个函数：

```javascript
console.log(string_sequence(0));  // 输出："0"
console.log(string_sequence(5));  // 输出：