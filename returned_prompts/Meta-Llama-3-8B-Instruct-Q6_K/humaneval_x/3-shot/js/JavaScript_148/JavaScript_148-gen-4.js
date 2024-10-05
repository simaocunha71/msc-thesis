  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  let planet1_index = planets.indexOf(planet1);
  let planet2_index = planets.indexOf(planet2);

  if (planet1_index === -1 || planet2_index === -1) {
    return [];
  }

  let start_index = Math.min(planet1_index, planet2_index);
  let end_index = Math.max(planet1_index, planet2_index);

  let result = planets.slice(start_index + 1, end_index);
  return result;
}