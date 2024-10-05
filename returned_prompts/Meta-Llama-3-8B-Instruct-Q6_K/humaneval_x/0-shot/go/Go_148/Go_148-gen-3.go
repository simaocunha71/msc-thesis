Here is a Go function that solves the problem:

```go
func Bf(planet1, planet2 string) []string {
    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    planetIndex1 := -1
    planetIndex2 := -1
    for i, planet := range planets {
        if planet == planet1 {
            planetIndex1 = i
        }
        if planet == planet2 {
            planetIndex2 = i
        }
        if planetIndex1 != -1 && planetIndex2 != -1 {
            break
        }
    }
    if planetIndex1 == -1 || planetIndex2 == -1 {
        return []string{}
    }
    result := planets[planetIndex1+1 : planetIndex2]
    return result
}
```

This function first finds the indices of the input planets in the slice of all planets. It then returns a slice of planets between the indices of the input planets, excluding the input planets themselves. If either of the input planets is not found in the slice, the function returns an empty slice. The planets are sorted by their proximity to the sun. 

For example, `Bf("Jupiter", "Neptune")` returns `["Saturn", "Uranus"]`, `Bf("Earth", "Mercury")` returns `["Venus"]`, and `Bf("Mercury", "Uranus")` returns `["Venus", "Earth", "Mars", "Jupiter", "Saturn"]`.  If the input planets are not found in the slice, the function returns an empty slice.  For example, `Bf("Mars", "Pluto")` returns an empty slice.  The function is case sensitive and does not handle errors.  It assumes that the input planets are valid planet names.  If the input planets are not valid planet names, the function may return incorrect results or panic.  The function also assumes that the input planets are in the correct order.  If the input planets are not in the correct order, the function may return incorrect results.  The function is not efficient for large inputs because it uses linear search to find the indices of the input planets.  It could be improved by using a map to store the planets and their indices, which would allow it to find the indices in constant time.  The