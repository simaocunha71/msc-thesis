```go
func Common(l1 []int, l2 []int) []int {
    set := make(map[int]bool)
    for _, v := range l1 {
        set[v] = true
    }
    common := []int{}
    for _, v := range l2 {
        if set[v] {
            common = append(common, v)
            delete(set, v)
        }
    }
    sort.Ints(common)
    return common
}
```
这段代码实现了找出两个列表的公共元素，并返回排序后的结果。

具体实现过程如下：
1. 创建一个空的map，用于存储列表l1中的元素。
2. 遍历列表l1，将每个元素作为键存入map中，值为true。
3. 创建一个空的切片common，用于存储公共元素。
4. 遍历列表l2，对于每个元素，判断是否在map中存在。如果存在，则将该元素加入common切片，并从map中删除该元素。
5. 对common切片进行排序。
6. 返回排序后的common切片。

这段代码的时间复杂度为O(n+m)，其中n和m分别为两个列表的长度。