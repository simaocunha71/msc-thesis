const bf = (planet1, planet2) => {
  // planet names
  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
  // empty array to store the planets
  let planetArray = []

  // check if planet1 and planet2 are correct planet names
  if (planets.includes(planet1) && planets.includes(planet2)) {
    // index of planet1 and planet2
    let planet1Index = planets.indexOf(planet1)
    let planet2Index = planets.indexOf(planet2)
    // loop through the planets array
    planets.forEach((planet, index) => {
      // check if planet is between planet1 and planet2
      if (planet1Index < index && planet2Index > index) {
        // add planet to the planetArray
        planetArray.push(planet)
      }
    })
  }
  return planetArray
}

