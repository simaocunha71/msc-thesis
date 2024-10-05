
    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    var idx1, idx2 int
    var ok1, ok2 bool

    for idx, planet := range planets {
        if planet == planet1 {
            idx1 = idx
            ok1 = true
        }
        if planet == planet2 {
            idx2 = idx
            ok2 = true
        }
    }

    if !ok1 || !ok2 {
        return []string{}
    }

    if idx1 > idx2 {
        idx1, idx2 = idx2, idx1
    }

    return planets[idx1+1 : idx2]
}
```

## Solution
```go
package kata

func BetweenPlanets(planet1, planet2 string) []string {

    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    var idx1, idx2 int
    var ok1, ok2 bool

    for idx, planet := range planets {
        if planet == planet1 {
            idx1 = idx
            ok1 = true
        }
        if planet == planet2 {
            idx2 = idx
            ok2 = true
        }
    }

    if !ok1 || !ok2 {
        return []string{}
    }

    if idx1 > idx2 {
        idx1, idx2 = idx2, idx1
    }

    return planets[idx1+1 : idx2]
}
```

## Test
```go
package kata

import (
    "testing"
    "reflect"
)

func TestBetweenPlanets(t *testing.T) {

    type test struct {
        input1, input2 string
        expected []string
    }

    tests := []test{
        {"Jupiter", "Neptune", []string{"Saturn", "Uranus"}},
        {"Earth", "Mercury