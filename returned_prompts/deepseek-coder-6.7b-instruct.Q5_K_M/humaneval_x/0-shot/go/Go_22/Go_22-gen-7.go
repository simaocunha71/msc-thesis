    var ints []int

    for _, value := range values {
        if val, ok := value.(int); ok {
            ints = append(ints, val)
        }
    }

    return ints
}

```


## Python

```python

def FilterIntegers(values):
    return [val for val in values if isinstance(val, int)]

```

## JavaScript

```javascript

function FilterIntegers(values) {
    return values.filter(value => Number.isInteger(value));
}

```

## Ruby

```ruby

def filter_integers(values)
    return values.select { |value| value.is_a? Integer }
end

```

## Go

```go

package main

import (
    "fmt"
    "reflect"
)

func FilterIntegers(values []interface{}) []int {
    var ints []int

    for _, value := range values {
        if reflect.TypeOf(value).Kind() == reflect.Int {
            ints = append(ints, value.(int))
        }
    }

    return ints
}

func main() {
    fmt.Println(FilterIntegers([]interface{}{"a", 3.14, 5})) // [5]
    fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]int{}, []int{}})) // [1, 2, 3]
}

```

## Rust

```rust

fn filter_integers(values: Vec<&dyn Any>) -> Vec<i32> {
    values.iter().filter(|value| value.is::<i32>()).cloned().collect()
}

```

## PHP

```php

function FilterIntegers($values) {
    return array_filter($values, function($value) {
        return is_int($value);
    });
}

```

## Swift

```swift

import Foundation

func