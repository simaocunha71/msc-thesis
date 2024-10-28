        StringBuilder result = new StringBuilder();
        for(int i = 0; i < a.length(); i++) {
            // XOR operation
            result.append((a.charAt(i) == b.charAt(i)) ? '0' : '1');
        }
        return result.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.stringXor("010", "110"));
    }
}

```

### Java位运算符

在Java中，位运算符用于操作整数的位。

以下是位运算符的列表：

1. `&` - 位与运算符。
2. `|` - 位或运算符。
3. `^` - 位异或运算符。
4. `~` - 位非运算符。
5. `<<` - 位左移运算符。
6. `>>` - 位右移运算符。
7. `>>>` - 零填充位右移运算符。

### Java的位运算符

Java中`^`（异或）运算符用于位运算，它对两个整数的每一位进行异或运算。

例如：

```java
int a = 5; // 二进制 101
int b = 3; // 二进制 011

int result = a ^ b; // 二进制 110
```

在上面的代码中，`a`和`b`的每一位都进行了异或运算。

### Java的位异或运算符

Java中的异或运算符`^`用于位运算。

当在两个操作数中，对应的位不相同时，该位被设置为1。

例如：

```java
int a = 5; // 二进制 101
int b = 3; // 二进制 011

int result = a ^ b; // 二进制 11