
    var result [][2]int

    for i, row := range lst {
        for j, value := range row {
            if value == x {
                result = append(result, [2]int{i, j})
            }
        }
    }

    sort.Slice(result, func(i, j int) bool {
        if result[i][0] < result[j][0] {
            return true
        }
        if result[i][0] > result[j][0] {
            return false
        }
        return result[i][1] > result[j][1]
    })

    return result
}

func main() {

    lst := [][]int{
        {1,2,3,4,5,6},
        {1,2,3,4,1,6},
        {1,2,3,4,5,1},
    }
    x := 1

    fmt.Println(GetRow(lst, x)) // [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
}

```

## 解法

我们首先创建一个空的`result`切片，用于保存行和列的索引，这些索引对应于`x`在`lst`中的出现位置。然后，我们遍历`lst`，检查每一行中的每个值。如果值等于`x`，我们将一个包含行索引和列索引的元组添加到`result`中。

最后，我们对`result`进行排序。首先，我们按行索引（元组的第一个元素）按升序排序。然后，对于每一行，我们按列索引（元组的第二个元素）按降序排序。

然后，我们返回排序后的`result`。

## 复杂度

时间复杂度为O(n*m)，其中n是行数，m是每行的平均列数。这是因为我们需要遍历输入矩阵的每个元素一次。

空间复杂度为O(k)，其中