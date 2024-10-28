        StringBuilder result = new StringBuilder();
        while (x > 0) {
            result.insert(0, x % base);
            x /= base;
        }
        return result.toString();
    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.changeBase(8, 3));
        System.out.println(s.changeBase(8, 2));
        System.out.println(s.changeBase(7, 2));
    }
}
```

## 解题思路

这个问题要求将一个十进制数转换为指定的进制数。我们可以通过使用除法和取模运算来解决这个问题。每次取模运算都会得到我们当前进制下的数字，我们可以将其插入到结果字符串的开头。然后我们将输入数字除以进制，重复这个过程，直到输入数字变为0。

## 复杂度分析

时间复杂度为 O(log_b(n))，其中 n 是输入数字。这是因为我们将输入数字除以进制，直到它变为0。空间复杂度为 O(log_b(n))，这是由于我们将数字转换为进制表示，并将其存储在一个字符串中。

## 参考

- [LeetCode 问题 476](https://leetcode.com/problems/number-complement/)
- [进制转换](https://en.wikipedia.org/wiki/Base_conversion)
- [转换为其他进制](https://www.rapidtables.com/convert/number/base-converter.html)

## 其他题目

- [LeetCode 405. 数字转换为十六进制](https://leetcode.com/problems/convert-a-number-to-hexadecimal/)
- [LeetCode 461. 汉明距离](https://leetcode.com/problems/hamming-distance/)
- [LeetCode 66. 加一](https://leetcode.com/problems