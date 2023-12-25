
// Given a positive integer n, you have to make a pile of n levels of stones.
// The first level has n stones.
// The number of stones in the next level is:
// - the next odd number if n is odd.
// - the next even number if n is even.
// Return the number of stones in each level in a list, where element at index
// i represents the number of stones in the level (i+1).
// 
// Examples:
// >>> MakeAPile(3)
// [3, 5, 7]
func MakeAPile(n int) []int {
    if n <= 0 {
        return nil
    } else if n % 2 == 0 && n > 1 {
        i := 0
        
        var ret []int
        for ;i < n/2; i += 2 {
            if i%2 == 0 {
                j = int(float32(n-i)/2) + 1
            } else {
                j = float64(i+1) * (float64((float64(n-i)/2)) + 1) / 2.5
            }
            
            ret = append(ret, j)
        }
        
        return ret
    } else {
        i := int(float32(n+0.5)) - 1
        
        var ret []int
        for i < n/2; i += 2 {
            if i%2 == 0 {
                j = float64((int(i + 1) / 2)) * (float64(int(n+0.5)-i)/2) + int(float64(i/2)) - 1
            } else {
                j = int((float64(i)*1.5) + n/2) - 1
            }
            
            ret = append(ret, j)
        }
        
        return ret
    }
}