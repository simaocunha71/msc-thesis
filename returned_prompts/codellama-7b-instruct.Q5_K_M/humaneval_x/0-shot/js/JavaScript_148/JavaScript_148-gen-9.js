const planets = {
  Mercury: 0,
  Venus: 1,
  Earth: 2,
  Mars: 3,
  Jupiter: 4,
  Saturn: 5,
  Uranus: 6,
  Neptune: 7,
};

return Object.keys(planets)
  .filter(
    planet =>
      planets[planet] > planets[planet1] && planets[planet] < planets[planet2]
  )
  .sort((a, b) => planets[a] - planets[b])
  .map(planet => [planet]);
}

// function bf(planet1, planet2) {
//   const planets = {
//     Mercury: 0,
//     Venus: 1,
//     Earth: 2,
//     Mars: 3,
//     Jupiter: 4,
//     Saturn: 5,
//     Uranus: 6,
//     Neptune: 7,
//   };

//   let listOfPlanets = [];
//   for (let planet in planets) {
//     if (planets[planet] > planets[planet1] && planets[planet] < planets[planet2]) {
//       listOfPlanets.push(planet);
//     }
//   }
//   listOfPlanets.sort((a, b) => planets[a] - planets[b]);
//   return listOfPlanets;
// }
