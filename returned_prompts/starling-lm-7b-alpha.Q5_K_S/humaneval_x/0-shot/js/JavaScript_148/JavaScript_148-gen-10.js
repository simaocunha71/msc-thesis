const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
if (!planets.includes(planet1) || !planets.includes(planet2)) {
  return [];
}
const idx1 = planets.indexOf(planet1);
const idx2 = planets.indexOf(planet2);
const res = planets.slice(Math.min(idx1, idx2) + 1, Math.max(idx1,