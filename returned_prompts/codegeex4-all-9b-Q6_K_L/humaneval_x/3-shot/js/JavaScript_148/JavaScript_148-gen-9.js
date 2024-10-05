  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const p1_index = planets.indexOf(planet1);
  const p2_index = planets.indexOf(planet2);

  if (p1_index == -1 || p2_index == -1) {
    return [];
  }

  var result = [];
  for (let i = Math.min(p1_index, p2_index) + 1; i < Math.max(p1_index, p2_index); i++) {
    result.push(planets[i]);
  }

  return result;
}