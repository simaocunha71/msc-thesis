  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const planetsIndex = planets.map((planet) => planets.indexOf(planet));

  if (planetsIndex.indexOf(planet1) === -1 || planetsIndex.indexOf(planet2) === -1) {
    return [];
  }

  const start = planetsIndex[planets.indexOf(planet1)];
  const end = planetsIndex[planets.indexOf(planet2)];

  return planets.slice(start + 1, end).reduce((acc, current) => acc.concat([current]), []);
}
//bf("Jupiter", "Neptune") should return ("Saturn", "Uranus") 
//bf("Earth", "Mercury") should return ("Venus")
//bf("Mercury", "Uranus") should return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")  //bf("Jupiter", "Neptune") should return ("Saturn", "Uranus")  //bf("Earth", "Mercury") should return ("Venus")  //bf("Mercury", "Uranus") should return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")  //bf("Jupiter", "Neptune") should return ("Saturn", "Uranus")  //bf("Earth", "Mercury") should return ("Venus")  //bf("Mercury", "Uranus") should return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
//bf("Jupiter", "Neptune") should return ("Saturn", "Uranus")  //bf("Earth", "Mercury") should return ("Venus")  //bf("Mercury", "Uranus") should return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")  //bf("Jupiter", "Neptune") should return ("Saturn", "Uranus")  //bf("Earth", "Mercury") should return ("Venus")  //bf("Mercury", "Uranus") should return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")  //bf("Jupiter", "Neptune") should return ("Saturn", "Uranus") 