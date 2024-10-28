    sort.Ints(arr)

B:
    sort.Sort(sort.Reverse(sort.IntSlice(arr)))

C:
    var strArr []string
    for _, v := range arr {
        if v < 1 || v > 9 {
            continue
        }
        strArr = append(strArr, []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}[v-1])
    }
    return strArr
}

```

## 题目解析

这是一道编程题，需要你按照以下步骤解题：

1. 首先，对数组进行升序排序。
2. 然后，对数组进行降序排序。
3. 接着，遍历排序后的数组，将每个在1到9范围内的数字转换为对应的中文数字名称，并将这些名称添加到一个新的字符串数组中。
4. 如果数组中包含超出1到9范围的数字，则忽略这些数字。
5. 最后，返回新字符串数组。

这道题目需要你熟悉Go语言中的排序库，以及数组和切片的使用。

## 参考答案

```go
func ByLength(arr []int) []string {

    // 对数组进行升序排序
    sort.Ints(arr)

    // 对数组进行降序排序
    sort.Sort(sort.Reverse(sort.IntSlice(arr)))

    // 创建一个新的字符串数组
    var strArr []string

    // 遍历排序后的数组
    for _, v := range arr {
        // 如果数字在1到9范围内，则将其转换为对应的中文数字名称并添加到新的数组中
        if v >= 1 && v <= 9 {
            strArr = append(strArr, []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",