
    sum := 0
    product := 1
    
    for _, num := range numbers {
        sum += num
        product *= num
    }
    
    return [2]int{sum, product}
}

```



## Swift

```swift
func sumProduct(numbers: [Int]) -> (Int, Int) {
    var sum = 0
    var product = 1
    
    for number in numbers {
        sum += number
        product *= number
    }
    
    return (sum, product)
}
```



## Java

```java
import java.util.*;

public class Main {
    public static int[] sumProduct(int[] numbers) {
        int sum = 0;
        int product = 1;
        
        for (int number: numbers) {
            sum += number;
            product *= number;
        }
        
        return new int[]{sum, product};
    }
    
    public static void main(String[] args) {
        int[] result = sumProduct(new int[]{1, 2, 3, 4});
        System.out.println(Arrays.toString(result));
    }
}
```



## JavaScript

```javascript
function sumProduct(numbers) {
    var sum = 0;
    var product = 1;
    
    for (var number of numbers) {
        sum += number;
        product *= number;
    }
    
    return [sum, product];
}
```



## Ruby

```ruby
def sum_product(numbers)
    sum = 0
    product = 1
    
    numbers.each { |number|
        sum += number
        product *= number
    }
    
    return [sum, product]
end
```



## PHP

```php
function sumProduct($numbers) {
    $sum = 0;
    $product = 1;
    
    foreach ($numbers as $number) {
        $sum += $number;
        $product *= $number;
    }
    
    return array($sum, $product);
}
```