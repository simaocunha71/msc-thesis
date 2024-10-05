  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);
  if (index1 === -1 || index2 === -1) return ();
  if (index1 > index2) [index1, index2] = [index2, index1];
  return planets.slice(index1 + 1, index2);
}
console.log(bf("Jupiter", "Neptune")); // ➞ ["Saturn", "Uranus"]
console.log(bf("Earth", "Mercury")); // ➞ ["Venus"]
console.log(bf("Mercury", "Uranus")); // ➞ ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]




A: Here's a JavaScript solution that uses the Array's `indexOf` method to find the indexes of `planet1` and `planet2` in the `planets` array. If either of them are not found, the function returns an empty array. If `planet1`'s index is greater than `planet2`'s, the function swaps the indexes. Finally, it slices the `planets` array from `planet1`'s index plus one (to exclude `planet1` itself) to `planet2`'s index and returns the result.

```javascript
const bf = (planet1, planet2) => {
  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);
  if (index1 === -1 || index2 === -1) return [];
  if (index1 > index2) [index1, index2] = [index2, index1];
  return planets.slice(index1 + 1, index2);
}

console.log(bf("J