Here's the solution using Python:

```python
def filterIntegers(values):
    return [value for value in values if isinstance(value, int)]
```

Here's the solution using JavaScript:

```javascript
const filterIntegers = (values) => {
  return values.filter(value => typeof value === 'number' && Number.isInteger(value));
};
```

Here's the solution using Java:

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static List<Integer> filterIntegers(List<Object> values) {
        List<Integer> result = new ArrayList<>();
        for (Object value : values) {
            if (value instanceof Integer) {
                result.add((Integer) value);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(filterIntegers(Arrays.asList(1, 2, 3, "abc", {}, new ArrayList<>())));
    }
}
```

Here's the solution using C#:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    public static List<int> FilterIntegers(List<object> values)
    {
        return values.OfType<int>().ToList();
    }

    public static void Main()
    {
        Console.WriteLine(string.Join(", ", FilterIntegers(new List<object> { 1, 2, 3, "abc", {}, new ArrayList<object>() })));
    }
}
```

These solutions iterate over the given list of values and filter out only the integers using the appropriate type checking and conversion functions for each programming language.