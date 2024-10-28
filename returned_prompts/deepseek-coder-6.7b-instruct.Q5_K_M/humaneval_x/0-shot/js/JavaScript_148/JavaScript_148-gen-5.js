  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
  const planet1Index = planets.indexOf(planet1)
  const planet2Index = planets.indexOf(planet2)
  
  if (planet1Index === -1 || planet2Index === -1) return ()
  
  return planets.slice(Math.min(planet1Index, planet2Index) + 1, Math.max(planet1Index, planet2Index))
}

console.log(bf("Jupiter", "Neptune"))  //==> 返回 ("Saturn", "Uranus")
console.log(bf("Earth", "Mercury"))  //==> 返回 ("Venus")
console.log(bf("Mercury", "Uranus"))  //==> 返回 ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
console.log(bf("Pluto", "Neptune"))  //==> 返回 ()
console.log(bf("Jupiter", "Pluto"))  //==> 返回 ()

*/

const bf = (planet1, planet2) => {
  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const planet1Index = planets.indexOf(planet1);
  const planet2Index = planets.indexOf(planet2);

  if (planet1Index === -1 || planet2Index === -1) return ();

  return planets.slice(Math.min(planet1Index, planet2Index) + 1, Math.max(planet1Index, planet2Index));
};

console.log(bf("Jupiter", "Neptune")); //==> 返回 ("Saturn", "Uranus")
console.log(bf("Earth", "Mercury")); //==> 返回 ("Venus")
console.log(bf("Mercury", "Uranus")); //==> 返回 ("Venus", "