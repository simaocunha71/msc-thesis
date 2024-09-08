  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  if (planets.indexOf(planet1) < 0 || planets.indexOf(planet2) < 0) {
    return [];
  }
  const i1 = planets.indexOf(planet1);
  const i2 = planets.indexOf(planet2);
  const res = [];
  for (let i = i1; i <= i2; ++i) {
    res.push(planets[i]);
  }
  return res;
}



