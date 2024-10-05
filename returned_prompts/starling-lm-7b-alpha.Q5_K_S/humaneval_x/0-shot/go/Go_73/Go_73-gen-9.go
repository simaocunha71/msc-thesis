
func SmallestChange(arr []int) int {
    left, right := 0, len(arr)-1
    count := 0
    for left < right {
        if arr[left] == arr[right] {
            left++
            right--
        } else {
            count += 1
            if arr[left] > arr[right] {
                arr[left] = arr[right]
            } else {
                arr[right] = arr[left]
            }
        }
    }
    return count
}

In this code, we use two pointers, left and right, to traverse the array from both ends simultaneously.
We initialize the count variable to 0, which will store the minimum number of elements needed to make the array palindromic.

While left is less than right, we compare the elements at the left and right pointers. If they are equal, we move the left pointer one step to the right and the right pointer one step to the left. If they are not equal, we increment the count variable by 1 and update the elements at the left and right pointers to make them equal. We do this by assigning the smaller element to the left pointer and the larger element to the right pointer.

Finally, we return the count variable, which represents the minimum number of elements needed to make the array palindromic.

The time complexity of this solution is O(n), where n is the length of the array, as we only traverse the array once. The space complexity is O(1), as we only use a constant amount of extra space to store the count variable.

This solution is efficient and has a low space complexity, making it suitable for solving the minimum number of elements needed to make an array palindromic problem.

I hope this helps! Let me know if you have any more questions.

*/

```

```python

```

```javascript

```

```csharp

```

```go

```

```java

```

```c

```

```cpp

```

```rust

```

```scala

```

```kotlin