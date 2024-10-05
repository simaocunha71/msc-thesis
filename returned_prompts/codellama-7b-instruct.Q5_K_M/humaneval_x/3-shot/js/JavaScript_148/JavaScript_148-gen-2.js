  var planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  var index1 = planets.indexOf(planet1);
  var index2 = planets.indexOf(planet2);
  if (index1 == -1 || index2 == -1) {
    return [];
  }
  var result = [];
  for (var i = index1; i <= index2; i++) {
    result.push(planets[i]);
  }
  return result;
}



