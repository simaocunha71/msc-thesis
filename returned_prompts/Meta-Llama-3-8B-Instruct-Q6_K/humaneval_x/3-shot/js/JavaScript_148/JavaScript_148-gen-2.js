  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  const planetIndex1 = planets.indexOf(planet1);
  const planetIndex2 = planets.indexOf(planet2);

  if (planetIndex1 === -1 || planetIndex2 === -1) {
    return [];
  }

  const start = Math.min(planetIndex1, planetIndex2);
  const end = Math.max(planetIndex1, planetIndex2) + 1;

  return planets.slice(start + 1, end).sort((a, b) => planets.indexOf(a) - planets.indexOf(b));
}