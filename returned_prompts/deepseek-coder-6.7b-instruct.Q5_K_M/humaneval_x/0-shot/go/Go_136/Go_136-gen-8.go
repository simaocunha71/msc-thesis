
largest := math.MinInt64
smallest := math.MaxInt64

for _, v := range lst {
  if v < 0 && v > largest {
    largest = v
  } else if v > 0 && v < smallest {
    smallest = v
  }
}

if largest == math.MinInt64 {
  largest = nil
}

if smallest == math.MaxInt64 {
  smallest = nil
}

return [2]interface{}{largest, smallest}

}

```



```python
# Python Solution

def largest_smallest_integers(lst):
    largest = float('-inf')
    smallest = float('inf')
    
    for v in lst:
        if v < 0 and v > largest:
            largest = v
        elif v > 0 and v < smallest:
            smallest = v
    
    if largest == float('-inf'):
        largest = None
        
    if smallest == float('inf'):
        smallest = None
    
    return (largest, smallest)

```




```javascript
// JavaScript Solution

function largestSmallestIntegers(lst) {
    let largest = Number.NEGATIVE_INFINITY;
    let smallest = Number.POSITIVE_INFINITY;

    for (let v of lst) {
        if (v < 0 && v > largest) {
            largest = v;
        } else if (v > 0 && v < smallest) {
            smallest = v;
        }
    }

    if (largest == Number.NEGATIVE_INFINITY) {
        largest = null;
    }

    if (smallest == Number.POSITIVE_INFINITY) {
        smallest = null;
    }

    return [largest, smallest];
}

```



```java
// Java Solution

import java.util.OptionalInt;

public class Main {
    public static void main(String[] args) {
        int[] list = {2, 4, 1, 3, 5