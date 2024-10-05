Here is the JavaScript solution for the problem:

```javascript
const bf = (planet1, planet2) => {
    const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
    const planetIndex1 = planets.indexOf(planet1);
    const planetIndex2 = planets.indexOf(planet2);

    if (planetIndex1 === -1 || planetIndex2 === -1) {
        return [];
    }

    if (planetIndex1 > planetIndex2) {
        [planetIndex1, planetIndex2] = [planetIndex2, planetIndex1];
    }

    const result = planets.slice(planetIndex1 + 1, planetIndex2).sort((a, b) => planets.indexOf(a) - planets.indexOf(b));

    return result.length > 0 ? result : [];
};

console.log(bf("Jupiter", "Neptune")); // Output: ["Saturn", "Uranus"]
console.log(bf("Earth", "Mercury")); // Output: ["Venus"]
console.log(bf("Mercury", "Uranus")); // Output: ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
```

This function first checks if the given planet names are valid by finding their indices in the `planets` array. If either of the planets is not found, the function returns an empty array. Then it checks if `planet1` is closer to the sun than `planet2`. If so, it swaps their indices. Finally, it slices the `planets` array from `planetIndex1 + 1` to `planetIndex2` (inclusive) and sorts the result. The function returns the sorted array of planets. If the array is empty, it returns an empty array. Otherwise, it returns the array of planets. The `bf` function is called with three different sets of planet names, and the results are logged to the console.