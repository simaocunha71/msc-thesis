  let planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  let idx1 = planets.indexOf(planet1);
  let idx2 = planets.indexOf(planet2);

  if (idx1 == -1 || idx2 == -1) {
    return [];
  }

  let start = Math.min(idx1, idx2) + 1;
  let end = Math.max(idx1, idx2);
  return planets.slice(start, end);
}



