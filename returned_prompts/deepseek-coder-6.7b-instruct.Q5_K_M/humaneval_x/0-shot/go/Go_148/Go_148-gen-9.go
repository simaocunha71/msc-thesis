
    planets := []string{
        "Mercury", "Venus", "Earth", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune",
    }

    var index1, index2 int
    var ok bool

    if index1, ok = planetsMap[planet1]; !ok {
        return []string{}
    }

    if index2, ok = planetsMap[planet2]; !ok {
        return []string{}
    }

    if index1 > index2 {
        index1, index2 = index2, index1
    }

    return planets[index1+1 : index2]
}

planetsMap := map[string]int{
    "Mercury": 0,
    "Venus":   1,
    "Earth":   2,
    "Mars":    3,
    "Jupiter": 4,
    "Saturn":  5,
    "Uranus":  6,
    "Neptune": 7,
}
```

## 2.

