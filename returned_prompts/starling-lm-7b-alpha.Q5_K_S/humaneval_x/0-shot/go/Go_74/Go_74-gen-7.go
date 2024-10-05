To solve this Kata, you'll need to:

Compare the lengths of the two input lists. If they have the same length, return the first list. If the length of the first list is greater than the second, return the second list. If the second list is greater than the first, return the first list.

Next, iterate over each element in the first list and add up the lengths of the strings in that list. Repeat the same process for the second list. Compare the sums of the lengths of the strings in each list. If the sum of the lengths in the first list is less than the second, return the first list. If the sum of the lengths in the second list is less than the first, return the second list.

Here's a step-by-step breakdown of the solution:

Create a variable len1 to store the length of the first list.
Create a variable len2 to store the length of the second list.
If len1 is equal to len2, return the first list.
If len1 is less than len2, return the first list.
If len1 is greater than len2, return the second list.
Create a variable sum1 to store the sum of the lengths of the strings in the first list.
Create a variable sum2 to store the sum of the lengths of the strings in the second list.
If sum1 is less than sum2, return the first list.
If sum1 is greater than sum2, return the second list.

Here's the code:

func TotalMatch(lst1 []string, lst2 []string) []string {
    len1 := len(lst1)
    len2 := len(lst2)
    if len1 == len2 {
        return lst1
    }
    if len1 < len2 {
        return lst1
    }
    if len1 > len2 {
        return lst2
    }
    sum1 := 0
    sum2 := 0
    for _, v := range lst1 {
        sum1 += len(v)
    }
    for _, v := range lst2 {
        sum2 += len(v)
    }
    if sum1 < sum2 {
        return lst1
    }
    if sum1 > sum2