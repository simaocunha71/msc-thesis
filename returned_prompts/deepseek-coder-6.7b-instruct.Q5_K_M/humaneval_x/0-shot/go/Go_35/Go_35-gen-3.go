
	max := l[0]
	for _, value := range l {
		if max < value {
			max = value
		}
	}
	return max
}

func main() {

	list := []int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}
	fmt.Println(MaxElement(list))
}

```

## Python

```python
# Python3 code to find maximum element in a list

def MaxElement(l):
    return max(l)

list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

print(MaxElement(list))
```

## JavaScript

```javascript
// JavaScript code to find maximum element in an array.

function MaxElement(l) {
    return Math.max(...l);
}

var list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10];

console.log(MaxElement(list));
```

## C#

```csharp
// C# code to find maximum element in a list.

using System;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
        List<int> list = new List<int>{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
        Console.WriteLine(MaxElement(list));
    }

    public static int MaxElement(List<int> l)
    {
        return l.Max();
    }
}
```

## Ruby

```ruby
# Ruby code to find maximum element in an array.

def MaxElement(l)
    return l.max
end

list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -