  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

  if (planets.includes(planet1) && planets.includes(planet2)) {
    const start = planets.indexOf(planet1)
    const end = planets.indexOf(planet2)
    return planets.slice(start, end + 1)
  } else {
    return () => {}
  }
}

console.log(bf("Jupiter", "Neptune")) //==> ("Saturn", "Uranus")
console.log(bf("Earth", "Mercury")) //==> ("Venus")
console.log(bf("Mercury", "Uranus")) //==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

// function bf(planet1, planet2) {
//   const planets = [
//     "Mercury",
//     "Venus",
//     "Earth",
//     "Mars",
//     "Jupiter",
//     "Saturn",
//     "Uranus",
//     "Neptune"
//   ];

//   if (!planets.includes(planet1) || !planets.includes(planet2)) return [];

//   const start = planets.indexOf(planet1);
//   const end = planets.indexOf(planet2);

//   return start < end ? planets.slice(start + 1, end) : planets.slice(end + 1, start);
// }

// console.log(bf("Jupiter", "Neptune")); //==> ("Saturn", "Uranus")
// console.log(bf("Earth", "Mercury")); //==> “Venus")
// console.log(bf("Mercury", "Uranus")); //==> “Venus", "Earth", "Mars", "Jupiter", "Saturn")































