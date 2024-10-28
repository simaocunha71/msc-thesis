
```go
planets := map[string]int{
    "Mercury": 0,
    "Venus": 1,
    "Earth": 2,
    "Mars": 3,
    "Jupiter": 4,
    "Saturn": 5,
    "Uranus": 6,
    "Neptune": 7,
}

if _, ok := planets[planet1]; !ok {
    return []string{}
}
if _, ok := planets[planet2]; !ok {
    return []string{}
}

var result []string
var prev = planets[planet1]
for k, v := range planets {
    if v >= prev && v <= planets[planet2] {
        result = append(result, k)
    }
    prev = v
}
return result
```

Explanation:

This program defines a map `planets` that stores the names of the planets as keys and their order in the solar system as values. When a planet name is passed as an argument, it checks if the planet is valid, if not it returns an empty result. Then it initializes a slice called `result` to store the planets that will be between the two planets passed as arguments. It also initializes a variable called `prev` to keep track of the previous planet order. Then it iterates through the `planets` map and if the current planet's order is between the orders of the two planets passed as arguments, it appends the planet's name to the `result` slice and updates the `prev` variable to the current planet's order. Finally, it returns the `result` slice with the names of the planets in the desired order.

The time complexity of this program is O(n) as it iterates through the `planets` map once. The space complexity is also O(n) as it stores the result in a slice.

```go
package main

import "fmt"

func main() {
    fmt.Println(Bf("Jupiter", "Neptune")) // ("Saturn", "Uranus")
    fmt.Println(Bf("Earth", "Mercury"))   // ("Venus")
    fmt.Print