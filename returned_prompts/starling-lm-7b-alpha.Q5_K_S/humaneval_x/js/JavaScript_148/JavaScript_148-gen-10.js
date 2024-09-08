  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  if (!planets.includes(planet1) || !planets.includes(planet2)) {
    return [];
  }
  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);
  if (index1 > index2) {
    return bf(planet2, planet1);
  }
  const result = [];
  for (let i = index1 + 1; i < index2; i++) {
    result.push(planets[i]);
  }
  return result;
}



