
	min, max := math.Inf(1), -math.Inf(1)
	for _, num := range numbers {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}

	rescaled := make([]float64, len(numbers))
	for i, num := range numbers {
		rescaled[i] = (num - min) / (max - min)
	}
	return rescaled
}

```


{{out}}

```txt

[0.0, 0.25, 0.5, 0.75, 1.0]

```



## Ruby


```ruby
def rescale_to_unit(numbers)
  min = numbers.min
  max = numbers.max
  numbers.map { |num| (num - min) / (max - min).to_f }
end

p rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
```


{{out}}

```txt

[0.0, 0.25, 0.5, 0.75, 1.0]

```



## Rust


```rust
fn rescale_to_unit(numbers: &mut [f64]) {
    let (mut min, mut max) = (numbers[0], numbers[0]);
    for &num in numbers.iter() {
        if num < min { min = num; }
        if num > max { max = num; }
    }
    let range = max - min;
    for num in numbers.iter_mut() {
        *num = (*num - min) / range;
    }
}

fn main() {
    let mut numbers = vec![1.0, 2.0, 3.0, 4.0, 5.0];
    rescale_to_unit(&mut numbers);
    for num in numbers {
        println¡{}
    }
}
```