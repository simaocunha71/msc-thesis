  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  const planet1_index = planets.indexOf(planet1);
  const planet2_index = planets.indexOf(planet2);

  if (planet1_index === -1 || planet2_index === -1) {
    return ();
  }

  const start = Math.max(0, planet1_index);
  const end = Math.min(planets.length - 1, planet2_index);

  return (planets.slice(start, end + 1));
}...



