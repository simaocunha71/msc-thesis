  let sum = numbers.reduce((a, b) => a + b, 0);
  let mean = sum / numbers.length;
  let differences = numbers.map(num => Math.abs(num - mean));
  let mad = differences.reduce((a, b) => a + b, 0) / numbers.length;
  return mad;
}

console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0]));
```

## Python

```python
def meanAbsoluteDeviation(numbers):
  mean = sum(numbers) / len(numbers)
  differences = [abs(num - mean) for num in numbers]
  mad = sum(differences) / len(differences)
  return mad

print(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0]))
```

## Ruby

```ruby
def meanAbsoluteDeviation(numbers)
  mean = numbers.reduce(:+) / numbers.length
  differences = numbers.map { |num| (num - mean).abs }
  mad = differences.reduce(:+) / numbers.length
  return mad
end

puts meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])
```

## JavaScript (ES6)

```javascript
const meanAbsoluteDeviation = numbers => {
  const mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  const differences = numbers.map(num => Math.abs(num - mean));
  const mad = differences.reduce((a, b) => a + b, 0) / numbers.length;
  return mad;
}

console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0]));
```

## Swift

```swift
import Foundation

func meanAbsoluteDeviation(numbers: [Double]) -> Double {
  let sum = numbers.reduce(0, +)
  let mean = sum