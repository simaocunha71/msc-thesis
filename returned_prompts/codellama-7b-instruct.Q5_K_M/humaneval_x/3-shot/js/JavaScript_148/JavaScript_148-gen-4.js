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
  const result = [];
  const p1 = planets[planet1];
  const p2 = planets[planet2];
  if (!p1 || !p2) {
    return [];
  }

  for (let i = 0; i <= p2 - p1; i++) {
    result.push(Object.keys(planets)[p1 + i]);
  }

  return result;
}



