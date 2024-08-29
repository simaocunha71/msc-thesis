  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  if (planets.includes(planet1) && planets.includes(planet2)) {
    const index1 = planets.indexOf(planet1);
    const index2 = planets.indexOf(planet2);
    if (index1 > index2) {
      [index1, index2] = [index2, index1];
    }
    const result = planets.slice(index1 + 1, index2);
    return result.join(', ');
  } else {
    return 'Invalid Planet names';
  }
}



