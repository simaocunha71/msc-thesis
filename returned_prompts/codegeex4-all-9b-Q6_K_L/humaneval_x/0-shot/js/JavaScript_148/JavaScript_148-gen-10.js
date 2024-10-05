```js
const bf = (planet1, planet2) => {
  let planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  let idx1 = planets.indexOf(planet1);
  let idx2 = planets.indexOf(planet2);
  if (idx1 === -1 || idx2 === -1) return [];
  let result = [];
  for (let i = Math.min(idx1, idx2) + 1; i < Math.max(idx1, idx2); i++) {
    result.push(planets[i]);
  }
  return result;
}
```