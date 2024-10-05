	sort.Ints(l)
	len := len(l)
	
	if len % 2 == 0 {
		return (float64(l[len/2-1]) + float64(l[len/2])) / 2.0
	} else {
		return float64(l[len/2])
	}
}


```


```python

def Median(l):
    l.sort()
    len_l = len(l)
    if len_l % 2 == 0:
        return (l[len_l//2-1] + l[len_l//2]) / 2.0
    else:
        return l[len_l//2]


```


```java

import java.util.Arrays;

public class Main {
    public static double Median(int[] l) {
        Arrays.sort(l);
        int len = l.length;
        if (len % 2 == 0) {
            return (l[len/2-1] + l[len/2]) / 2.0;
        } else {
            return l[len/2];
        }
    }

    public static void main(String[] args) {
        int[] arr = {3, 1, 2, 4, 5};
        System.out.println(Median(arr));
    }
}

```


```csharp

using System;
using System.Linq;

class Program {
    static double Median(int[] l) {
        Array.Sort(l);
        int len = l.Length;
        if (len % 2 == 0) {
            return (l[len/2-1] + l[len/2]) / 2.0;
        } else {
            return l[len/2];
        }
    }

    static void Main() {
        int[] arr = {3, 1, 2, 4, 5};
        Console.WriteLine(Median(arr));
    }
}

```


```javascript

function Median(l) {
    l.