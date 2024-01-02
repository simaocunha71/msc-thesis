
// Write a function that returns true if the object q will fly, and false otherwise.
// The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.
// 
// Example:
// WillItFly([1, 2], 5) ➞ false
// 1+2 is less than the maximum possible weight, but it's unbalanced.
// 
// WillItFly([3, 2, 3], 1) ➞ false
// it's balanced, but 3+2+3 is more than the maximum possible weight.
// 
// WillItFly([3, 2, 3], 9) ➞ true
// 3+2+3 is less than the maximum possible weight, and it's balanced.
// 
// WillItFly([3], 5) ➞ true
// 3 is less than the maximum possible weight, and it's balanced.
func WillItFly(q []int,w int) bool {
    if len(q) == 0 || w > q[len(q)-1]+q{
        return false
    }
    
    
    sum := make([]int, len(q))
    
    for i:=0;i<len(q);i++ {
        sum[i] = q[i]+sum[i-1];
        
        if w <= sum[i]{
            return true
        }
    }
    return false;
}
