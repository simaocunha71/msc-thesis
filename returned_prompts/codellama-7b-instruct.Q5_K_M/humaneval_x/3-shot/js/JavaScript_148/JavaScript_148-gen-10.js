  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const planet1_index = planets.indexOf(planet1);
  const planet2_index = planets.indexOf(planet2);
  if (planet1_index == -1 || planet2_index == -1) {
    return [];
  }
  const result = [];
  for (let i = planet1_index; i <= planet2_index; i++) {
    result.push(planets[i]);
  }
  return result;
}



