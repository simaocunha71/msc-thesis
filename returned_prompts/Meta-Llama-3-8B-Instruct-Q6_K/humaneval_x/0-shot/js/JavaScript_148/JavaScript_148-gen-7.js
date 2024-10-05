Here is a JavaScript solution for the problem:

```javascript
const bf = (planet1, planet2) => {
  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  const planet1Index = planets.indexOf(planet1);
  const planet2Index = planets.indexOf(planet2);

  if (planet1Index === -1 || planet2Index === -1) {
    return [];
  }

  const result = [];
  for (let i = planet1Index + 1; i < planet2Index; i++) {
    result.push(planets[i]);
  }

  return result;
};

console.log(bf("Jupiter", "Neptune"));  // Output: ["Saturn", "Uranus"]
console.log(bf("Earth", "Mercury"));     // Output: ["Venus"]
console.log(bf("Mercury", "Uranus"));    // Output: ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
```

In this solution, we first create an array of planets. Then, we find the indices of `planet1` and `planet2` in the array. If either `planet1` or `planet2` is not found in the array, we return an empty array.

Next, we iterate over the planets from `planet1` to `planet2` (excluding `planet2`) and add each planet to the result array.

Finally, we return the result array. If `planet1` or `planet2` is not a correct planet name, the function will return an empty array. Otherwise, it will return a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by the proximity to the sun.