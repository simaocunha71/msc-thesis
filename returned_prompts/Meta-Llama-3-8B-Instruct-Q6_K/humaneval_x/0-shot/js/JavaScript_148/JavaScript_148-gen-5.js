Here is a JavaScript solution for the problem:

```javascript
const bf = (planet1, planet2) => {
  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  const planetIndex1 = planets.indexOf(planet1);
  const planetIndex2 = planets.indexOf(planet2);

  if (planetIndex1 === -1 || planetIndex2 === -1) {
    return [];
  }

  const start = Math.min(planetIndex1, planetIndex2);
  const end = Math.max(planetIndex1, planetIndex2);

  return planets.slice(start + 1, end).reduce((acc, current) => {
    acc.push(current);
    return acc;
  }, []);
};
```

This function first finds the indices of the given planet names in the `planets` array. If either planet is not found, it returns an empty array. Then it determines the start and end indices of the range of planets to be returned. It uses the `slice` method to get the slice of the `planets` array between the start and end indices, and then uses the `reduce` method to convert the slice to an array. The result is returned as a tuple.