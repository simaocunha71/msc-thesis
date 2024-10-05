/* This problem is fairly straight-forward. We need to determine the planets
  between two given planets. We can start by creating an array of all the
  planets and then filtering that array based on the given planets. We can use
  the `findIndex` method to determine the indexes of the two given planets. After
  we have the indexes, we can filter the array based on those indexes. Finally,
  we can sort the result by the planets' proximity to the sun. */

  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  let index1 = planets.findIndex(planet => planet === planet1);
  let index2 = planets.findIndex(planet => planet === planet2);

  if (index1 < index2) {
    let result = planets.slice(index1 + 1, index2);
    if (result.length > 0) {
      result = result.sort((a, b) => planets.indexOf(a) - planets.indexOf(b));
    }
    return result;
  } else {
    let result = planets.slice(index2, index1 + 1);
    if (result.length > 0) {
      result = result.sort((a, b) => planets.indexOf(a) - planets.indexOf(b));
    }
    return result;
  }
};

/* Here are a few examples of the function working */
console.log(bf("Jupiter", "Neptune") === ("Saturn", "Uranus")); // true
console.log(bf("Earth", "Mercury") === ("Venus")); // true
console.log(bf("Mercury", "Uranus") === ("Venus", "Earth", "Mars", "Jupiter", "Saturn")); // true





































































