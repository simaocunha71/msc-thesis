    var sum float64 = 0
    var mean float64 = 0
    var mad float64 = 0

    for _, num := range numbers {
        sum += num
    }

    mean = sum / float64(len(numbers))

    for _, num := range numbers {
        mad += math.Abs(num - mean)
    }

    return mad / float64(len(numbers))
}
```

## 3. 算法复杂性分析

上述算法的时间复杂度为 O(n)，因为它需要对数组进行两次遍历。空间复杂度为 O(1)，因为它只需要常数的空间来存储和计算平均值和偏差。

## 4. 测试

在Go中，你可以使用 `testing` 包来编写测试。

```go
import (
    "testing"
    "math"
)

func TestMeanAbsoluteDeviation(t *testing.T) {
    var tests = []struct {
        input    []float64
        expected float64
    }{
        {[]float64{1.0, 2.0, 3.0, 4.0}, 1.0},
        {[]float64{5.0, 10.0, 100.0}, 70.0},
        {[]float64{-1.0, -2.0, -3.0, -4.0}, 1.0},
    }

    for _, test := range tests {
        if output := MeanAbsoluteDeviation(test.input); output != test.expected {
            t.Errorf("Test Failed: %v inputted, %v expected, recieved: %v", test.input, test.expected, output)
        }
    }
}
```

在上面的测试中，我们将不同的输入传递给我们的 `MeanAbsoluteDeviation` 函数，并验证输出是否与预期值相匹配。如果不匹配，将打印错误消息。

## 5. 执行

你可以将上述代码复制粘贴到一个名为 `