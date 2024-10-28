  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  const planet1Index = planets.indexOf(planet1);
  const planet2Index = planets.indexOf(planet2);
  if (planet1Index === -1 || planet2Index === -1) {
    return [];
  }
  if (planet1Index > planet2Index) {
    [planet1Index, planet2Index] = [planet2Index, planet1Index];
  }
  return planets.slice(planet1Index + 1, planet2Index).sort((a, b) => planets.indexOf(a) - planets.indexOf(b));
}