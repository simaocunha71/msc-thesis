  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  let p1_index = planets.indexOf(planet1);
  let p2_index = planets.indexOf(planet2);
  if (p1_index == -1 || p2_index == -1) {
    return [];
  }
  if (p1_index > p2_index) {
    [p1_index, p2_index] = [p2_index, p1_index];
  }
  return planets.slice(p1_index + 1, p2_index);
}