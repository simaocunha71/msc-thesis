
	res := make([]int, len(l))
	for i, v := range l {
		res[i] = v + 1
	}
	return res
}

// End of the function.

```


## Go

```go
package main

import "fmt"

func IncrList(l []int) []int {
	res := make([]int, len(l))
	for i, v := range l {
		res[i] = v + 1
	}
	return res
}

func main() {
	fmt.Println(IncrList([]int{1, 2, 3})) // [2, 3, 4]
	fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123})) // [6, 4, 6, 3, 4, 4, 10, 1, 124]
}
```


## Javascript

```javascript
function IncrList(l) {
  return l.map(x => x + 1);
}

console.log(IncrList([1, 2, 3])); // [2, 3, 4]
console.log(IncrList([5, 3, 5, 2, 3, 3, 9, 0, 123])); // [6, 4, 6, 3, 4, 4, 10, 1, 124]
```


## Julia

```julia
function IncrList(l)
  return [x+1 for x in l]
end

println(IncrList([1, 2, 3])) # [2, 3, 4]
println(IncrList([5, 3, 5, 2, 3, 3, 9, 0, 123])) # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```


## Kotlin