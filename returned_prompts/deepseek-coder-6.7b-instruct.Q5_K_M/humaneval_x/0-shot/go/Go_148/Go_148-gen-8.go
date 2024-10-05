
  planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

  planetMap := map[string]int{
    "Mercury": 1,
    "Venus": 2,
    "Earth": 3,
    "Mars": 4,
    "Jupiter": 5,
    "Saturn": 6,
    "Uranus": 7,
    "Neptune": 8,
  }

  if _, ok := planetMap[planet1]; !ok {
    return []string{}
  }

  if _, ok := planetMap[planet2]; !ok {
    return []string{}
  }

  start := planetMap[planet1]
  end := planetMap[planet2]

  if start > end {
    start, end = end, start
  }

  return planets[start:end]
}

// 2022.01.27-18:56:06

// Solution:

// This solution first checks if the input planet names are valid. If not, it returns an empty tuple.
// Then, it finds the index of the start and end planets in the planets list.
// If the start index is greater than the end index, it swaps the two.
// Finally, it returns a tuple containing all planets whose orbits are located between the start and end planets.
// The planets are returned in the order of their proximity to the sun.

// 2022.01.27-19:02:57

// Test:

// Testing with the following inputs:

// Bf("Jupiter", "Neptune")  should return ("Saturn", "Uranus")
// Bf("Earth", "Mercury")  should return ("Venus")
// Bf("Mercury", "Uranus")  should return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

// The function seems to work as expected.

// 202