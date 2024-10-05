const bf = (planet1, planet2) => {
  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  if (!planets.includes(planet1) || !planets.includes(planet2)) return [];
  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);
  const planetsBetween = [];
  for (let i = index1 + 1; i < index2; i++) {
    planetsBetween.push(planets[i])
  }
  return planetsBetween;
}
