
    if a == 0 {
        return b
    }

    return GreatestCommonDivisor(b % a, a)
}

func main() {
    fmt.Println(GreatestCommonDivisor(3, 5)) // should print 1
    fmt.Println(GreatestCommonDivisor(25, 15)) // should print 5
}
```

#### Python

```python
def greatest_common_divisor(a, b):

    while(b): 
        a, b = b, a % b

    return a

print(greatest_common_divisor(3, 5)) # should print 1
print(greatest_common_divisor(25, 15)) # should print 5
```

#### Java

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(greatestCommonDivisor(3, 5)); // should print 1
        System.out.println(greatestCommonDivisor(25, 15)); // should print 5
    }

    public static int greatestCommonDivisor(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return greatestCommonDivisor(b, a % b);
        }
    }
}
```

#### JavaScript

```javascript
function greatestCommonDivisor(a, b) {
    if (b == 0) {
        return a;
    } else {
        return greatestCommonDivisor(b, a % b);
    }
}

console.log(greatestCommonDivisor(3, 5)); // should print 1
console.log(greatestCommonDivisor(25, 15)); // should print 5
```

#### Ruby

```ruby
def greatest_common_divisor(a, b)
    return a if b == 0
    return greatest_common_divisor(b, a % b)
end

puts greatest_common_divisor(3, 5) # should print 1
puts greatest_common_divisor(25, 15)