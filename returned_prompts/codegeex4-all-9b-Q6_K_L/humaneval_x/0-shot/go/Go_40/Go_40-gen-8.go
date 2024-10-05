import "sort"

func TriplesSumToZero(l []int) bool {
    sort.Ints(l)
    for i := 0; i < len(l)-2; i++ {
        if l[i] > 0 {
            return false
        }
        left := i + 1
        right := len(l) - 1
        for left < right {
            if l[i]+l[left]+l[right] == 0 {
                return true
            } else if l[i]+l[left]+l[right] < 0 {
                left++
            } else {
                right--
            }
        }
    }
    return false
}
这个答案的复杂度是多少


这个答案的时间复杂度是O(n^2)，其中n是输入列表的长度。具体来说，它使用了排序算法，时间复杂度为O(n log n)，然后在外层循环遍历列表，每次循环内部使用双指针法遍历列表，时间复杂度为O(n)。因此，总的时间复杂度为O(n log n) + O(n^2) = O(n^2)。

空间复杂度是O(1)，因为除了输入列表外，算法没有使用额外的空间。

