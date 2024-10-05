  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);
  if (index1 == -1 || index2 == -1) {
    return [];
  }
  if (index1 > index2) {
    const temp = index1;
    index1 = index2;
    index2 = temp;
  }
  return planets.slice(index1 + 1, index2);
}