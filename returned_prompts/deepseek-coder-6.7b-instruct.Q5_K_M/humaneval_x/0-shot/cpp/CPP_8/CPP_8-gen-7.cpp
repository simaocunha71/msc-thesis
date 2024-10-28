    int sum = 0;
    int product = 1;
    for(int i = 0; i < numbers.size(); i++){
        sum += numbers[i];
        product *= numbers[i];
    }
    return {sum, product};
}
int main(){
    vector<int> numbers = {1, 2, 3, 4};
    vector<int> result = sum_product(numbers);
    printf("(%d, %d)\n", result[0], result[1]);
    return 0;
}
```

### Ruby

```ruby
# Ruby
def sum_product(numbers)
  return 0, 1 if numbers.empty?
  sum = numbers.reduce(:+)
  product = numbers.reduce(:*)
  [sum, product]
end

puts sum_product([]).inspect
puts sum_product([1, 2, 3, 4]).inspect
```

### JavaScript

```javascript
// JavaScript
function sum_product(numbers) {
  if (numbers.length === 0) return [0, 1];
  let sum = 0;
  let product = 1;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }
  return [sum, product];
}

console.log(sum_product([]));
console.log(sum_product([1, 2, 3, 4]));
```

### Python

```python
# Python
def sum_product(numbers):
    if not numbers:
        return 0, 1
    sum_numbers = sum(numbers)
    product_numbers = 1
    for num in numbers:
        product_numbers *= num
    return sum_numbers, product_numbers

print(sum_product([]))
print(sum_product([1, 2, 3, 4]))
```

### Java

```java
import java.util.List;

public class Main {
    public static void main(String[] args