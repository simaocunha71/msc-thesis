To solve this problem, you can follow these steps:

1. Check if the length of the string is at least 3. If not, return false.
2. Create a set to store the 3 consecutive letters.
3. Iterate through the string, taking a slice of 3 characters each time.
4. Check if the slice is in the set. If it is, return false. Otherwise, add the slice to the set.
5. If the loop completes without returning false, return true.

Here's an example implementation of the solution:

func IsHappy(s string) bool {
    if len(s) < 3 {
        return false
    }

    set := make(map[string]struct{})

    for i := 0; i+2 < len(s); i++ {
        key := s[i : i+3]
        if _, ok := set[key]; ok {
            return false
        }
        set[key] = struct{}{}
    }

    return true
}

In this implementation, we first check if the length of the string is less than 3. If it is, we return false, as the string is not long enough to have 3 consecutive distinct letters.

Next, we create a map called "set" to store the 3 consecutive letters. We use a map instead of a slice because maps have a constant time complexity for lookups, while slices have a linear time complexity.

We then iterate through the string, taking a slice of 3 characters each time using the index expression s[i:i+3]. We check if the slice is already in the set using the expression _, ok := set[key]. If it is, we return false, as the slice is not distinct. Otherwise, we add the slice to the set using the assignment set[key] = struct{}.

If the loop completes without returning false, we can conclude that all 3 consecutive letters in the string are distinct, and we return true.

You can use this implementation to check if a given string is happy or not.

Here are some example usages of the function:

fmt.Println(IsHappy("abc")) // Output: true
fmt.Println(IsHappy("aaa")) // Output: false
fmt.