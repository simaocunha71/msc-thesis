  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  if (planets.includes(planet1) && planets.includes(planet2)) {
    let start = planets.indexOf(planet1);
    let end = planets.indexOf(planet2);
    if (start > end) {
      [start, end] = [end, start];
    }
    return planets.slice(start + 1, end + 1).join(', ');
  }
  return "";
}



