    var count [2]int
    numStr := strconv.Itoa(num)
    for _, v := range numStr {
        if (int(v)-'0')%2 == 0 {
            count[0]++
        } else {
            count[1]++
        }
    }
    return count
}

func main() {
    fmt.Println(EvenOddCount(-12))  //==> 输出：[1 1]
    fmt.Println(EvenOddCount(123))  //==> 输出：[1 2]
}
```

## 相关题目

- [计算整数的位数](https://www.codewars.com/kata/56b22765e1007b79f2000079/train/go)
- [计算整数的位数](https://www.codewars.com/kata/56b22765e1007b79f2000079/train/python)
- [计算整数的位数](https://www.codewars.com/kata/56b22765e1007b79f2000079/train/javascript)
- [计算整数的位数](https://www.codewars.com/kata/56b22765e1007b79f2000079/train/ruby)
- [计算整数的位数](https://www.codewars.com/kata/56b22765e1007b79f2000079/train/java)
- [计算整数的位数](https://www.codewars.com/kata/56b22765e1007b79f2000079/train/csharp)
- [计算整数的位数](https://www.codewars.com/kata/56b22765e1007b79f2000