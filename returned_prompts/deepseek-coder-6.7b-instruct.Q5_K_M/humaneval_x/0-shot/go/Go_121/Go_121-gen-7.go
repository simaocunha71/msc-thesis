
    var sum int
    for i := 0; i < len(lst); i+=2 {
        if lst[i] % 2 != 0 {
            sum += lst[i]
        }
    }
    return sum
}
```

### Python

```python
def Solution(lst):
    return sum(el for i, el in enumerate(lst) if i % 2 == 0 and el % 2 != 0)
```

### JavaScript

```javascript
function Solution(lst){
    var sum = 0;
    for(var i = 0; i < lst.length; i += 2){
        if(lst[i] % 2 !== 0){
            sum += lst[i];
        }
    }
    return sum;
}
```

### Ruby

```ruby
def Solution(lst)
    sum = 0
    lst.each_index do |i|
        if i % 2 == 0 && lst[i] % 2 != 0
            sum += lst[i]
        end
    end
    return sum
end
```

### Java

```java
public class Main {
    public static int Solution(int[] lst) {
        int sum = 0;
        for (int i = 0; i < lst.length; i += 2) {
            if (lst[i] % 2 != 0) {
                sum += lst[i];
            }
        }
        return sum;
    }
}
```

### C#

```csharp
public static int Solution(int[] lst)
{
    int sum = 0;
    for (int i = 0; i < lst.Length; i += 2)
    {
        if (lst[i] % 2 != 0)
        {
            sum += lst[i];
        }
    }
    return sum;
}
```

### Kotlin

```kotlin
fun Solution(lst: IntArray): Int {
    var sum = 0
    for (i in 0..