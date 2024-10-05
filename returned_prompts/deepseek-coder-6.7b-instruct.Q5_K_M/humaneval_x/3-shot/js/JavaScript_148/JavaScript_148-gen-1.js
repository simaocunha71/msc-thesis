  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const planet1_index = planets.indexOf(planet1);
  const planet2_index = planets.indexOf(planet2);

  if (planet1_index ≥ 0  && planet2_index ≥ 0) {
    return planets.slice(Math.min(planet1_index, planet2_index), Math.max(planet1_index, planet2_index));
  } else {
    return ();
  }
}
```


