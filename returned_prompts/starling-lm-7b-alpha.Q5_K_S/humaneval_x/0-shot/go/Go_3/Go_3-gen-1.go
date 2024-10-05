
    balance := 0
    for _, op := range operations {
        balance += op
        if balance < 0 {
            return true
        }
    }
    return false
}








```

```

```

```go
package main

import (
    "fmt"
)

func BelowZero(operations []int) bool {
    balance := 0
    for _, op := range operations {
        balance += op
        if balance < 0 {
            return true
        }
    }
    return false
}

func main() {
    fmt.Println(BelowZero([]int{1, 2, 3}))
    fmt.Println(BelowZero([]int{1, 2, -4, 5}))
}
```

```python
def BelowZero(operations):
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

```javascript
function BelowZero(operations) {
    let balance = 0;
    for (let op of operations) {
        balance += op;
        if (balance < 0) {
            return true;
        }
    }
    return false;
}
```
```

```

```csharp
using System;
public class Program
{
    public static void Main()
    {
        Console.WriteLine(BelowZero(new[] { 1, 2, 3 }));
        Console.WriteLine(BelowZero(new[] { 1, 2, -4, 5 }));
    }
    public static bool BelowZero(int[] operations)
    {
        int balance = 0;
        foreach (int op in operations)
        {
            balance += op;
            if (balance < 0)
            {
                return true;
            }
        }
        return false;
    }
}
```

```cpp
#include <iostream>

bool BelowZero(std::vector<int> operations)
{
    int balance = 0;
    for