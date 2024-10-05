```java
const bf = (planet1, planet2) => {
  var planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
  var p1 = planets.indexOf(planet1)
  var p2 = planets.indexOf(planet2)
  if (p1 === -1 || p2 === -1 || p1 === p2) return []
  var res = []
  if (p1 < p2) {
    for (let i = p1 + 1; i < p2; i++) {
      res.push(planets[i])
    }
  } else {
    for (let i = p2 + 1; i < p1; i++) {
      res.push(planets[i])
    }
  }
  return res
}
```