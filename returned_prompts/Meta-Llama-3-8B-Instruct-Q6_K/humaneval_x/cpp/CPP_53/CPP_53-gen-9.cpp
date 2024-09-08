    return x+y;
}

main() {
    printf("%d\n", add(2,3));
    printf("%d\n", add(5,7));
    return 0;
}

```

C:
```c
#include <stdio.h>

int add(int x, int y) {
    return x + y;
}

int main() {
    printf("%d\n", add(2, 3));
    printf("%d\n", add(5, 7));
    return 0;
}
```

Python:
```python
def add(x, y):
    return x + y

print(add(2, 3))
print(add(5, 7))
```

Java:
```java
public class Main {
    public static int add(int x, int y) {
        return x + y;
    }

    public static void main(String[] args) {
        System.out.println(add(2, 3));
        System.out.println(add(5, 7));
    }
}
```

JavaScript:
```javascript
function add(x, y) {
    return x + y;
}

console.log(add(2, 3));
console.log(add(5, 7));
```

Ruby:
```ruby
def add(x, y)
    x + y
end

puts add(2, 3)
puts add(5, 7)
```

PHP:
```php
function add($x, $y) {
    return $x + $y;
}

echo add(2, 3)."\n";
echo add(5, 7)."\n";
```

Go:
```go
package main

import "fmt"

func add(x int, y int) int {
    return x + y
}

func main() {
    fmt.Println(add(2, 3))
    fmt.Println(add(5, 7))
}
```

Swift:
```swift
func add(x: Int, y: Int) -> Int {
    return x + y
}

print(add(x: 2, y: 3))
print(add(x: 5, y: 7))
```

C++:
```c++
#include <iostream>

int add(int x, int y) {
    return x + y;
}

int main() {
    std::cout << add(2, 3) << std::endl;
    std::cout << add(5, 7) << std::endl;
    return 0;
}
```



In this code, we