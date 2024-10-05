  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  
  if (!planets.includes(planet1) || !planets.includes(planet2)) return ();
  
  const i1 = planets.indexOf(planet1);
  const i2 = planets.indexOf(planet2);
  
  if (i1 < i2) return planets.slice(i1 + 1, i2);
  else return planets.slice(i2 + 1, i1);
}

console.log(bf("Jupiter", "Neptune")); //==> 출력: [ 'Saturn', 'Uranus' ]
console.log(bf("Earth", "Mercury")); //==> 출력: [ 'Venus' ]
console.log(bf("Mercury", "Uranus")); //==> 출력: [ 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn' ]

```

This function works by first checking that the inputs are valid planet names. If they are not, it returns an empty tuple. Then, it gets the indexes of the planet names in the planets array. It slices the array from the next index of the smaller index to the next index of the larger index, and returns the result. The result is sorted by the proximity to the sun.


## 2. Create a function that takes a number n and a string s as arguments and returns a new string that is n copies of the string s.

```javascript
