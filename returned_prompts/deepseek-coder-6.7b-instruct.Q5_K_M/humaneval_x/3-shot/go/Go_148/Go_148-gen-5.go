    planets  := []string{
        "Mercury", "Venus", "Earth", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune",
    }

    planet1Index, planet2Index := -1, -1
    for i, planet := range planets  {
        if planet == planet1  {
            planet1Index = i
        } else if planet == planet2  {
            planet2Index = i
        }
    }

    if planet1Index == -1 || planet2Index == -1  {
        return []string{}
    }

    if planet1Index > planet2Index  {
        planet1Index, planet2Index = planet2Index, planet1Index
    }

    return planets[planet1Index+1 : planet2Index]
}



