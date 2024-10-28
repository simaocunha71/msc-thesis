  smallest_even := math.MaxInt32
  smallest_even_index := -1
  for i, v := range arr {
    if v % 2 == 0 && v < smallest_even {
      smallest_even = v
      smallest_even_index = i
    }
  }
  if smallest_even_index == -1 {
    return []int{}
  }
  return []int{smallest_even, smallest_even_index}
}

```


### JavaScript

```javascript
// JavaScript Solution

var pluck = function(arr) {
  let smallest_even = Number.MAX_SAFE_INTEGER;
  let smallest_even_index = -1;
  for(let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0 && arr[i] < smallest_even) {
      smallest_even = arr[i];
      smallest_even_index = i;
    }
  }
  if (smallest_even_index == -1) {
    return [];
  }
  return [smallest_even, smallest_even_index];
};

```


### Python

```python
# Python Solution

def pluck(arr):
  smallest_even = float('inf')
  smallest_even_index = -1
  for i, v in enumerate(arr):
    if v % 2 == 0 and v < smallest_even:
      smallest_even = v
      smallest_even_index = i
  if smallest_even_index == -1:
    return []
  return [smallest_even, smallest_even_index]
```


### Ruby

```ruby
# Ruby Solution

def pluck(arr)
  smallest_even = Float::INFINITY
  smallest_even_index = -1
  arr.each_with_index do |v, i|
    if v % 2 == 0 && v < smallest_even
      smallest_even = v
      smallest_even_index = i
    end
  end
  return [] if smallest_even_index == -1