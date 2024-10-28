  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);

  if (index1 == -1 || index2 == -1) {
    return [];
  }

  const result = [];
  for (let i = index1 + 1; i < index2; i++) {
    result.push(planets[i]);
  }
  for (let i = index2 - 1; i > index1; i--) {
    result.push(planets[i]);
  }

  return result;
}



