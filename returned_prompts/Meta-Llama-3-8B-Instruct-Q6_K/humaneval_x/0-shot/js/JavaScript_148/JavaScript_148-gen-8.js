Here is the solution:
```javascript
const bf = (planet1, planet2) => {
  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);

  if (index1 === -1 || index2 === -1) {
    return [];
  }

  const start = Math.min(index1, index2);
  const end = Math.max(index1, index2);

  return planets.slice(start + 1, end);
};
```
Here's an explanation of the code:

1. We first define an array `planets` that contains all the planet names in the correct order.
2. We find the indices of `planet1` and `planet2` in the `planets` array using the `indexOf` method. If either of the indices is -1, it means the planet name is not correct, so we return an empty array.
3. We calculate the start and end indices based on the smaller and larger indices of `planet1` and `planet2`.
4. We use the `slice` method to extract the planets between the start and end indices, and return the result as a tuple.

You can test the function with the examples you provided:
```javascript
console.log(bf("Jupiter", "Neptune")); // ["Saturn", "Uranus"]
console.log(bf("Earth", "Mercury")); // ["Venus"]
console.log(bf("Mercury", "Uranus")); // ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
```