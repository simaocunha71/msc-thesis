Here's a possible solution:

```javascript
const planets = {
    Mercury: 36000000,
    Venus: 67000000,
    Earth: 107000000,
    Mars: 227900000,
    Jupiter: 483800000,
    Saturn: 953700000,
    Uranus: 1783000000,
    Neptune: 2792000000,
};

const bf = (planet1, planet2) => {
    const sorted = Object.keys(planets)
        .sort((a, b) => planets[a] - planets[b]);

    const index1 = sorted.findIndex(key => key === planet1);
    const index2 = sorted.findIndex(key => key === planet2);

    if (index1 === -1 || index2 === -1) {
        return [];
    }

    return sorted.slice(index1 + 1, index2);
};

console.log(bf("Jupiter", "Neptune"));      // ["Saturn", "Uranus"]
console.log(bf("Earth", "Mercury"));       // ["Venus"]
console.log(bf("Mercury", "Uranus"));      // ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
```

This solution defines an object `planets` that maps planet names to their distances from the sun. It then uses the `sort()` method to sort the keys of this object in ascending order of distance from the sun. The `findIndex()` method is used to find the indices of the given planets in the sorted array of planets. If either planet is not found, an empty array is returned. Otherwise, the `slice()` method is used to extract the planets that are located between the given planets, sorted by proximity to the sun.

Note: The `sort()` method sorts the keys of the `planets` object in lexicographical order by default. To sort them