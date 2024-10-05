
sum := 0

B:

for i := 1; i <= n; i++ {

C:

sum += i

}

D:

return sum

}

```

Here is the Python code that computes the sum of numbers from 1 to n:

```python
def SumToN(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
```

Here is the JavaScript code that computes the sum of numbers from 1 to n:

```javascript
function SumToN(n) {
    let sum = 0;
    for (let i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}
```

Here is the Java code that computes the sum of numbers from 1 to n:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(SumToN(30));
    }

    public static int SumToN(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}
```

Here is the C++ code that computes the sum of numbers from 1 to n:

```c++
#include<iostream>
using namespace std;
int SumToN(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}
int main() {
    cout << SumToN(30);
    return 0;
}
```

These programs all do the same thing, they sum the numbers from 1 to n. The logic of the loop and the summing operation is the same in all of them.

This is a simple problem that can be solved using loops in all the mentioned languages, but the syntax and structure of the code can be different.

Please note that this problem can be solved in a more efficient way using mathematical formulas, but this solution provides an