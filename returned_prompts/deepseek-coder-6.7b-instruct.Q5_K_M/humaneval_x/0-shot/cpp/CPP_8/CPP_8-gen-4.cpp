    int sum = 0, product = 1;
    for(int i=0; i<numbers.size(); i++){
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

### Python:

```python
def sum_product(numbers):
    sum_val = 0
    product = 1
    for num in numbers:
        sum_val += num
        product *= num
    return (sum_val, product)

print(sum_product([]))
print(sum_product([1, 2, 3, 4]))
```

### JavaScript:

```javascript
function sumProduct(numbers) {
    var sum = 0, product = 1;
    for(var i = 0; i < numbers.length; i++) {
        sum += numbers[i];
        product *= numbers[i];
    }
    return [sum, product];
}

console.log(sumProduct([]));
console.log(sumProduct([1, 2, 3, 4]));
```

### Java:

```java
import java.util.List;

class Main {
    public static void main(String[] args) {
        System.out.println(sumProduct(new int[]{}));
        System.out.println(sumProduct(new int[]{1, 2, 3, 4}));
    }

    public static int[] sumProduct(int[] numbers) {
        int sum = 0;
        int product = 1;
        for(int number : numbers){
            sum += number;
            product *= number;
        }
        return new int[]{sum, product};
    }
}
```

### Ruby:

```ruby
def sum_product(numbers)
    sum = 0
    product = 1
   