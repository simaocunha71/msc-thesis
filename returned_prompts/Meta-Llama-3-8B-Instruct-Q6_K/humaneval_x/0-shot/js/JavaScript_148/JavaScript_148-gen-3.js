Here is a JavaScript function that meets the requirements:
```
const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];

const bf = (planet1, planet2) => {
  if (!planets.includes(planet1) || !planets.includes(planet2)) {
    return [];
  }

  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);

  if (index1 > index2) {
    [index1, index2] = [index2, index1];
  }

  const result = planets.slice(index1 + 1, index2);
  return result;
};
```
Here's an explanation of the code:

1. We define an array `planets` that contains the names of the planets in our solar system, in the correct order.
2. The `bf` function takes two planet names as strings, `planet1` and `planet2`, and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by proximity to the sun.
3. We first check if `planet1` or `planet2` are not correct planet names by using the `includes` method to check if they exist in the `planets` array. If either of them is not a valid planet name, we return an empty tuple.
4. We then find the indices of `planet1` and `planet2` in the `planets` array using the `indexOf` method.
5. We swap the indices if `planet1` is located after `planet2` in the array, so that `index1` is always the smaller index.
6. We use the `slice` method to extract the planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`. We start from `index1 + 1` (to exclude `planet1`) and end at `index2` (to exclude `planet2`).
7. We return the resulting array of planets, which is a tuple of strings.

You can test the function with the examples you provided:
```
console.log(bf("Jupiter", "Neptune")); // ["Saturn", "Uranus"]
console.log(bf("Earth", "Mercury")); // ["Venus"]
console.log(bf("Mercury", "