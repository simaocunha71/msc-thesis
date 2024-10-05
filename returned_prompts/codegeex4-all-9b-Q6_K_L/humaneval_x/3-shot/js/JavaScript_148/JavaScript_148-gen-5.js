  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  var planet1_index = planets.indexOf(planet1);
  var planet2_index = planets.indexOf(planet2);

  if (planet1_index == -1 || planet2_index == -1) {
    return [];
  }

  var start_index = Math.min(planet1_index, planet2_index);
  var end_index = Math.max(planet1_index, planet2_index);

  return planets.slice(start_index + 1, end_index);
}