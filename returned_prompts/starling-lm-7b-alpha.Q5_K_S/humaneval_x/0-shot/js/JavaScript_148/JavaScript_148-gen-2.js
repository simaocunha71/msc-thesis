const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
const index1 = planets.indexOf(planet1);
const index2 = planets.indexOf(planet2);

if (index1 === -1 || index2 === -1) {
  return [];
}

const result = planets.slice(Math.min(index1, index2) + 1, Math.max(index1, index2));
return result;

};

*/

To solve this Kata, you should follow these test.

Examples

bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
bf("Earth", "Mercury") ==> ("Venus")
bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

In this problem, we can follow these steps to solve it.

1. Create an array called "planets" and store all the planet names in order from the nearest to the sun to the furthest.
2. Create a function called "bf" that takes two planet names as arguments. These names will be stored in variables called "planet1" and "planet2".
3. Use the indexOf() method to find the position of "planet1" and "planet2" in the "planets" array. If either of the planets is not found in the array, return an empty array.
4. Create a variable called "result" and use the slice() method to create a new array that starts at the index of the smaller planet and ends at the index of the larger planet. This will give us all the planets that orbit between the two given planets.
5. Return the "result" array.



*/

const bf = (planet1, planet2) => {

  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);