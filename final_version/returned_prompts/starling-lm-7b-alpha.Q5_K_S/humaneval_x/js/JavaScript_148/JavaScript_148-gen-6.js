  let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

  if (planets.indexOf(planet1) < 0 || planets.indexOf(planet2) < 0) {
    return [];
  }

  let min_index = planets.indexOf(planet1);
  let max_index = planets.indexOf(planet2);

  let min_value = min_index;
  let max_value = max_index;

  while (min_value < max_value && planets[min_value + 1] == planets[min_value]) {
    min_value += 1;
  }
  while (max_value > min_value && planets[max_value - 1] == planets[max_value]) {
    max_value -= 1;
  }

  let result = [];
  for (let i = min_value; i <= max_value; i++) {
    result.push(planets[i]);
  }

  return result;
}



