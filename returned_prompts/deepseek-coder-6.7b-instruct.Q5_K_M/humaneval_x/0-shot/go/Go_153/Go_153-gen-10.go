    max := math.MinInt32
    strongest := ""
    for _, ext := range extensions {
        CAP, SM := 0, 0
        for _, c := range ext {
            if 'A' <= c && c <= 'Z' {
                CAP++
            } else if 'a' <= c && c <= 'z' {
                SM++
            }
        }
        strength := CAP - SM
        if strength > max {
            max = strength
            strongest = ext
        }
    }
    return class_name + "." + strongest
}
```

## 解题思路

本题要求我们找出具有最强扩展的类。“强度”定义为大写字母的数量减去小写字母的数量。我们遍历所有扩展，计算它们的强度，并跟踪具有最高强度的扩展。如果有多个具有相同强度的扩展，我们选择首先出现的那个。

## 复杂度分析

由于我们只遍历一次扩展列表，所以时间复杂度为O(n)，其中n是扩展的数量。空间复杂度也为O(n)，因为我们存储了扩展的列表。

## 参考

1. [Go语言标准库](https://golang.org/pkg/)

2. [Golang编程语言](https://golang.org/)

3. [Golang编程技巧](https://golang.org/doc/effective_go)

4. [Golang面试题](https://golang.org/doc/code.html)

5. [Golang编程练习](https://www.w3resource.com/go-exercises/)

6. [Golang语言基础](https://www.cnblogs.com/poloyy/p/8799248.html)

7. [Golang学习路线](https://www.golang-china.org/learn-go)

8. [Golang教程](https://tour.golang.org/welcome/1)

9. [Golang代码示例](