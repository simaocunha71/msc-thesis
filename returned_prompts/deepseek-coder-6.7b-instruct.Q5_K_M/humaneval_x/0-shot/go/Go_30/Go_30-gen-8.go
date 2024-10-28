
	result := []int{}
	for _, v := range l {
		if v > 0 {
			result = append(result, v)
		}
	}
	return result
}
```

**Python:**

```python
# Python

def get_positive(l):
    return [n for n in l if n > 0]

print(get_positive([-1, 2, -4, 5, 6]))  # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # [5, 3, 2, 3, 9, 123, 1]
```

**C#:**

```C#
// C#
using System;
using System.Linq;

public class Program
{
	public static void Main()
	{
		int[] numbers = new int[] {-1, 2, -4, 5, 6};
		var posNumbers = GetPositive(numbers);
		Console.WriteLine(string.Join(", ", posNumbers));

		numbers = new int[] {5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
		posNumbers = GetPositive(numbers);
		Console.WriteLine(string.Join(", ", posNumbers));
	}

	public static int[] GetPositive(int[] numbers)
	{
		return numbers.Where(n => n > 0).ToArray();
	}
}
```

**JavaScript:**

```javascript
// JavaScript
function getPositive(arr) {
    return arr.filter(num => num > 0);
}

console.log(getPositive([-1, 2, -4, 5, 6]));  // [2, 5, 6]
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123