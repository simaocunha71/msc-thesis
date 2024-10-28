    for i, num := range nums {
        nums[i] = strconv.Itoa(num)
    }
    type point struct {
        num  int
        sum  int
        idx  int
    }
    type bySum []point
    sort.Sort(bySum(nums))
    return nil


func OrderByPoints(nums []int) []int {
    type point struct {
        num  int
        sum  int
        idx  int
    }
    type bySum []point
    sort.Sort(bySum(nums))
    return nil
}


func OrderByPoints(nums []int) []int {
    type point struct {
        num  int
        sum  int
        idx  int
    }
    type bySum []point
    sort.Sort(bySum(nums))
    return nil
}


func OrderByPoints(nums []int) []int {
    type point struct {
        num  int
        sum  int
        idx  int
    }
    type bySum []point
    sort.Sort(bySum(nums))
    return nil
}



Ans:
To sort the given list of integers in ascending order according to the sum of their digits, you can use the following steps:

1. Iterate through the input array and convert each integer into a string. This will allow us to calculate the sum of its digits. You can use the `strconv.Itoa()` function to convert an integer to a string.

2. Create a custom type called `point` with three fields: `num`, `sum`, and `idx`. The `num` field represents the original integer, the `sum` field represents the sum of the digits, and the `idx` field represents the index of the integer in the original array.

3. Create another custom type called `bySum` which is a slice of `point`. This type will be used as the key type for the `sort.Sort()` function.

4. Use the `sort.Sort()` function to sort the `bySum` slice in ascending order based on the `sum` field of each `point`. The `sort.Sort()` function