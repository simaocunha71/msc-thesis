  const planetsOrder = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const planet1Index = planetsOrder.indexOf(planet1);
  const planet2Index = planetsOrder.indexOf(planet2);

  if (planet1Index === -1 || planet2Index === -1) {
    return ();
  }

  return planetsOrder.slice(Math.min(planet1Index, planet2Index) + 1, Math.max(planet1Index, planet2Index));
}



