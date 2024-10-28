const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];

const bf = (planet1, planet2) => {
  let index1 = planets.indexOf(planet1);
  let index2 = planets.indexOf(planet2);
  
  if (index1 === -1 || index2 === -1) {
    return [];
  }
  
  if (index1 > index2) {
    [index1, index2] = [index2, index1];
  }
  
  return planets.slice(index1 + 1, index2);
}

console.log(bf("Jupiter", "Neptune")); //==> ("Saturn", "Uranus")
console.log(bf("Earth", "Mercury")); //==> ("Venus")
console.log(bf("Mercury", "Uranus")); //==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")