You can use the following solution:

```go
func Bf(planet1, planet2 string) []string {
    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    for i, planet := range planets {
        if planet == planet1 {
            return planets[i+1 : len(planets)-1-i]
        }
        if planet == planet2 {
            return planets[i+1 : len(planets)-1-i]
        }
    }
    return nil
}
```

This solution first creates a slice of all the planets in the order of their distance from the Sun. Then, it iterates through the slice until it finds either planet1 or planet2. If it finds planet1, it returns a slice of the planets between planet1 and the end of the slice. If it finds planet2, it returns a slice of the planets between planet2 and the end of the slice. If it doesn't find either planet1 or planet2, it returns nil.

Note that the indices used in the slice are based on the distance from the Sun, not the index in the slice. This is because the planets are sorted in order of their distance from the Sun.