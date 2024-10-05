
    result := make([]int, 0, len(numbers)*2-1)
    for i, num := range numbers {
        result = append(result, num)
        if i < len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}


```

## 4. 使用Go语言编写一个函数，将两个整数列表合并为一个新的列表，其中每个元素是输入列表中对应元素的和。

