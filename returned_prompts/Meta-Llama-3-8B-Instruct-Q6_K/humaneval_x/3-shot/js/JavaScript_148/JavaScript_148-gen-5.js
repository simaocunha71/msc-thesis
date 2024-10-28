  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const correctPlanets = planets.filter(p => p === planet1 || p === planet2);
  if (correctPlanets.length !== 2) return tuple();

  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);

  if (index1 === -1 || index2 === -1) return tuple();

  let result = [];
  for (let i = index1 + 1; i < index2; i++) {
    result.push(planets[i]);
  }
  return tuple(...result);
}

function tuple(...args) {
  return args;
}