```js
const bf = (planet1, planet2) => {
  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);
  if (index1 === -1 || index2 === -1 || index1 === index2) return [];
  const start = Math.min(index1, index2) + 1;
  const end = Math.max(index1, index2);
  return planets.slice(start, end);
}
```
