  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const planet_index1 = planets.indexOf(planet1);
  const planet_index2 = planets.indexOf(planet2);
  if (planet_index1 == -1 || planet_index2 == -1) {
    return [];
  }
  const planet_list = [];
  for (let i = planet_index1; i <= planet_index2; i++) {
    planet_list.push(planets[i]);
  }
  return planet_list;
}



