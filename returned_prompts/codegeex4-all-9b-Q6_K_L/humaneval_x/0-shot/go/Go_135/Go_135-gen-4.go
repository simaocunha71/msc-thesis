func CanArrange(arr []int) int {
    last := arr[0]
    for i := 1; i < len(arr); i++ {
        if arr[i] < last {
            return i - 1
        }
        last = arr[i]
    }
    return -1
}

I got the right answer but I don't think I did it the right way.

I was thinking that I had to sort the array, but then I thought that it wouldn't be the right way.

I'm new to Go and I'm trying to learn, so I'm open to any feedback or suggestions. I'm just looking for the best solution.

