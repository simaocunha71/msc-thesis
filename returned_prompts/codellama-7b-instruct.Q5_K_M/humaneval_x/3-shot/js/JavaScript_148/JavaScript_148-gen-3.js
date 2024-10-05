  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

  if (planets.includes(planet1) && planets.includes(planet2)) {
    const planet1_index = planets.indexOf(planet1);
    const planet2_index = planets.indexOf(planet2);

    if (planet1_index < planet2_index) {
      return planets.slice(planet1_index + 1, planet2_index);
    } else {
      return planets.slice(planet2_index + 1, planet1_index);
    }
  } else {
    return [];
  }
}



